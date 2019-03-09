from constant.templates import UserData, LogMessage
from balebot.utils.logger import Logger
from configs import BotConfig

logger = Logger.get_logger()


def step_success(response, user_data):
    user_data = user_data[UserData.kwargs]
    user_peer = user_data[UserData.user_peer]
    step_name = user_data[UserData.step_name]
    logger.info(LogMessage.successful_step_message_sending.format(step_name),
                extra={UserData.user_id: user_peer.peer_id, UserData.step_name: step_name, "tag": "info"})
    if user_data.get(UserData.succedent_message):
        bot = user_data[UserData.bot]
        step_name = user_data[UserData.step_name]
        succedent_message = user_data[UserData.succedent_message]
        kwargs = {UserData.user_peer: user_peer, UserData.step_name: step_name,
                  UserData.message: succedent_message, UserData.attempt: 1,
                  UserData.logger: logger, UserData.bot: bot}
        bot.send_message(message=succedent_message, peer=user_peer, success_callback=step_success,
                         failure_callback=step_failure, kwargs=kwargs)


def step_failure(response, user_data):
    user_data = user_data[UserData.kwargs]
    user_peer = user_data[UserData.user_peer]
    step_name = user_data[UserData.step_name]
    bot = user_data[UserData.bot]
    message = user_data[UserData.message]
    user_data[UserData.attempt] += 1
    if user_data[UserData.attempt] < BotConfig.resending_max_try:
        bot.send_message(message=message, peer=user_peer, success_callback=step_success, failure_callback=step_failure,
                         kwargs=user_data)
        return
    logger.error(LogMessage.failed_step_message_sending.format(step_name),
                 extra={UserData.user_id: user_peer.peer_id, UserData.step_name: step_name, "tag": "error"})
