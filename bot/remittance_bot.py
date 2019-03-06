import re
import asyncio

from balebot.filters import TemplateResponseFilter, TextFilter, BankMessageFilter, DefaultFilter
from balebot.handlers import MessageHandler, CommandHandler
from balebot.models.base_models import UserPeer
from balebot.models.messages import TemplateMessage, TextMessage, PurchaseMessage, BankMessage, TemplateResponseMessage
from balebot.models.messages.banking.money_request_type import MoneyRequestType
from balebot.updater import Updater

from configs import BotConfig
from constant.templates import BotTexts, BotButtons, Step, ButtonText, BotMessages, provinces_to_branch_dict
from bot.call_backs import step_success, step_failure
from balebot.utils.logger import Logger
from database.operations import user_was_logged, add_payment_to_db, get_payment_with_message_id, update_payment_is_done, \
    message_id_is_repetitive, insert_to_table
from database.tables import Users
from utils.utils import change_rial_to_afghan_currency, eng_to_arabic_number, generate_random_number_with_N_digits, \
    thousand_separator

loop = asyncio.get_event_loop()
updater = Updater(token=BotConfig.bot_token, loop=loop)
dispatcher = updater.dispatcher
logger = Logger.get_logger()


# +++++++++++++++++++++++++ send_message ++++++++++++++++++++++++++++++++#

def send_message(message, peer, step, succedent_message=None):
    bot = dispatcher.bot
    kwargs = {"user_peer": peer, "step_name": step, "succedent_message": succedent_message,
              "message": message, "attempt": 1, "bot": bot}
    bot.send_message(message=message, peer=peer, success_callback=step_success,
                     failure_callback=step_failure, kwargs=kwargs)


# ++++++++++++++++++++++++++++++++++ start_bot ++++++++++++++++++++++++++++ #
# @dispatcher.message_handler(
#     [TemplateResponseFilter(BotButtons.back_to_main_menu), TextFilter(["/start", BotTexts.back_to_main_menu])])
@dispatcher.message_handler(DefaultFilter())
def start_bot_for_users_that_do_not_logged_in(bot, update):
    user_peer = update.get_effective_user()
    was_logged = user_was_logged(user_id=user_peer.peer_id)

    if was_logged:
        start_bot_for_logged_in_users(bot, update)
    else:
        buttons_list = [BotButtons.register, BotButtons.help]
        template_message = TemplateMessage(TextMessage(BotTexts.welcome_message), buttons_list)
        send_message(message=template_message, peer=user_peer, step=Step.start_bot_for_users_that_do_not_logged_in)
        dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
            MessageHandler(filters=[TemplateResponseFilter(keywords=[BotButtons.register.value])],
                           callback=request_user_name),
            MessageHandler(filters=[TemplateResponseFilter(keywords=BotButtons.help.value)], callback=usage_help)
        ])


def usage_help(bot, update):
    user_peer = update.get_effective_user()
    buttons_list = [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(general_message=TextMessage(BotTexts.help_message), btn_list=buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.help)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers)


def request_user_name(bot, update):
    user_peer = update.get_effective_user()
    buttons_list = [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotTexts.enter_your_name), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.register)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), get_name_from_user),
    ])


def get_name_from_user(bot, update):
    user_peer = update.get_effective_user()
    user_name = update.get_effective_message().text
    user_id = user_peer.peer_id
    access_hash = user_peer.access_hash
    insert_to_table(Users(name=user_name, user_id=user_id, access_hash=access_hash))
    start_bot_for_logged_in_users(bot, update)


def start_bot_for_logged_in_users(bot, update):
    user_peer = update.get_effective_user()
    buttons_list = [BotButtons.remittance, BotButtons.help]
    template_message = TemplateMessage(TextMessage(BotTexts.choose_one_option), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.start_bot_for_logged_in_users)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TemplateResponseFilter(BotButtons.remittance.value), request_sender_name),
        MessageHandler(TemplateResponseFilter(BotButtons.help.value), usage_help)
    ])


def request_sender_name(bot, update):
    user_peer = update.get_effective_user()
    text_message = TextMessage(BotTexts.enter_sender_name)
    send_message(message=text_message, peer=user_peer, step=Step.request_sender_name)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), request_money_changer),
    ])


def request_money_changer(bot, update):
    user_peer = update.get_effective_user()
    sender_name = update.get_effective_message().text
    dispatcher.set_conversation_data(update, key="sender_name", value=sender_name)
    buttons_list = [BotButtons.money_changer, BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotTexts.choose_one_money_changer), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.start_resistance_conversation)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TemplateResponseFilter(BotButtons.money_changer.value), request_receiver_name)
    ])


def request_receiver_name(bot, update):
    user_peer = update.get_effective_user()
    money_changer = update.get_effective_message().text
    dispatcher.set_conversation_data(update, key="money_changer", value=money_changer)
    buttons_list = [BotButtons.back_to_main_menu]
    general_message = TextMessage(BotTexts.enter_receiver_name)
    template_message = TemplateMessage(general_message, buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.start_resistance_conversation)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), request_province)
    ])


def request_province(bot, update):
    user_peer = update.get_effective_user()
    receiver_name = update.get_effective_message().text
    dispatcher.set_conversation_data(update, key="receiver_name", value=receiver_name)
    buttons_list = BotButtons.cities + [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotTexts.enter_city_name), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.get_receiver_name)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TemplateResponseFilter(keywords=[city.value for city in BotButtons.cities]), request_branch)
    ])


def request_branch(bot, update):
    user_peer = update.get_effective_user()
    city_name = update.get_effective_message().text
    dispatcher.set_conversation_data(update, key="city_name", value=city_name)
    buttons_list = [BotButtons.back_to_main_menu]
    branch_address = provinces_to_branch_dict.get(city_name)
    template_message = TemplateMessage(TextMessage(branch_address), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.get_receiver_name)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), request_amount),
    ])


def request_amount(bot, update):
    user_peer = update.get_effective_user()
    branch_id = update.get_effective_message().text
    dispatcher.set_conversation_data(update, key="branch_address", value=branch_id)
    buttons_list = [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotTexts.enter_amount), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.get_city_name)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), send_payment_message)
    ])


def send_payment_message(bot, update):
    user_peer = update.get_effective_user()
    amount = update.get_effective_message().text
    if amount.isnumeric():
        dispatcher.set_conversation_data(update, key="amount", value=amount)
        owner_user_id = user_peer.peer_id
        receiver_name = dispatcher.get_conversation_data(update, "receiver_name")
        city_name = dispatcher.get_conversation_data(update, "city_name")
        sender_name = dispatcher.get_conversation_data(update, "sender_name")
        branch_address = dispatcher.get_conversation_data(update, "branch_address")

        photo_message = BotMessages.money_request_photo_message
        # owner = get_owner_with_user_id(owner_user_id)
        afghan_currency_amount = eng_to_arabic_number(
            thousand_separator(int(change_rial_to_afghan_currency(rial=int(amount), currency=140))))

        message_id = generate_random_number_with_N_digits(6)
        while message_id_is_repetitive(message_id):
            message_id = generate_random_number_with_N_digits(6)

        add_payment_to_db(owner_user_id=owner_user_id, receiver_name=receiver_name, city_name=city_name, amount=amount,
                          message_id=message_id)
        amount_message = eng_to_arabic_number(thousand_separator(amount))
        money_request_caption = BotTexts.money_request_caption.format(eng_to_arabic_number(message_id),
                                                                      sender_name, receiver_name,
                                                                      city_name, branch_address, amount_message,
                                                                      eng_to_arabic_number(afghan_currency_amount))

        photo_message.caption_text = TextMessage(money_request_caption)

        purchase_message = PurchaseMessage(account_number=BotConfig.money_changer_account_number, amount=amount,
                                           money_request_type=MoneyRequestType.normal, msg=photo_message)
        # These are for next version.
        # kwargs = {"user_peer": user_peer, "step_name": Step.get_payment_amount_with_valid_input,
        #           "succedent_message": None,
        #           "message": purchase_message, "attempt": 1, "bot": bot, "update": update}
        # bot.send_message(message=purchase_message, peer=user_peer, success_callback=step_success,
        #                  failure_callback=step_failure,
        #                  kwargs=kwargs)
        send_message(message=purchase_message, peer=user_peer, step=Step.get_payment_amount)
        dispatcher.finish_conversation(update)

    else:
        template_message = TemplateMessage(TextMessage(BotTexts.invalid_input), [BotButtons.back_to_main_menu])
        send_message(message=template_message, peer=user_peer, step=Step.get_payment_amount)
        dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
            MessageHandler(TextFilter(), send_payment_message)
        ])


@dispatcher.message_handler(BankMessageFilter())
def send_report(bot, update):
    # update = test_update_2
    message = update.get_effective_message()
    user_peer = update.get_effective_user()
    user_id = user_peer.peer_id
    if isinstance(message, BankMessage) and int(user_id) == 11:
        receipt = message.get_receipt()
        message_id = receipt.regarding.splitlines()[0]
        print(message_id)
        message_id = int(re.search(r'\d+', message_id).group())
        print(message_id)
        payment = get_payment_with_message_id(message_id)
        owner = payment.owner
        owner_user = UserPeer(peer_id=owner.user_id, access_hash=owner.access_hash)
        money_changer_user_id = 776725385
        money_changer_access_hash = "-3564513944394449112"
        muhammad_user_id = 1314892980
        muhammad_access_hash = "6115941441665528566"
        money_changer = UserPeer(peer_id=money_changer_user_id, access_hash=money_changer_access_hash)
        muhammad = UserPeer(peer_id=muhammad_user_id, access_hash=muhammad_access_hash)

        afghan_amount = eng_to_arabic_number(int(change_rial_to_afghan_currency(int(payment.money_amount), 140)))
        money_amount = eng_to_arabic_number(thousand_separator(payment.money_amount))
        report_message = TextMessage(
            BotTexts.report_message.format(payment.receiver_name, payment.destination_city_name,
                                           eng_to_arabic_number(message_id),
                                           afghan_amount, money_amount,
                                           BotTexts.payment_date))
        update_payment_is_done(message_id)
        print(report_message.text)

        send_message(report_message, money_changer, Step.send_report)
        send_message(report_message, owner_user, Step.send_report)
        send_message(report_message, muhammad, Step.send_report)
        dispatcher.register_conversation_next_step_handler(update, handlers=[
                                                                                MessageHandler(TextFilter(
                                                                                    BotTexts.back_to_main_menu),
                                                                                    start_bot_for_logged_in_users)
                                                                            ] + common_handlers)


common_handlers = [
    CommandHandler(commands=["/start"], callback=start_bot_for_users_that_do_not_logged_in),
    MessageHandler(TemplateResponseFilter(ButtonText.back), callback=start_bot_for_users_that_do_not_logged_in)
]
