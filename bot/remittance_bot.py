import re
import jdatetime
from balebot.filters import TemplateResponseFilter, TextFilter, BankMessageFilter, PhotoFilter
from balebot.handlers import MessageHandler, CommandHandler
from balebot.models.base_models import FatSeqUpdate, UserPeer
from balebot.models.messages import TemplateMessage, TextMessage, PurchaseMessage, BankMessage, PhotoMessage, \
    TemplateResponseMessage
from balebot.models.messages.banking.money_request_type import MoneyRequestType
from balebot.updater import Updater
import asyncio
from configs import BotConfig
from bot.templates import BotMessages, BotButtons, LogMessage, Step, test_update_2
from bot.call_backs import step_success, step_failure
from balebot.utils.logger import Logger
from database.operations import add_user_to_bot, user_was_logged, add_payment_to_db, get_owner_with_user_id, \
    get_payment_with_message_id, update_payment_is_done, generate_message_id, message_id_is_repetitive
from utils.utils import change_rial_to_afghan_currency, eng_to_arabic_number, generate_random_number_with_N_digits, thousand_separator

loop = asyncio.get_event_loop()
updater = Updater(token=BotConfig.bot_token, loop=loop)
dispatcher = updater.dispatcher
logger = Logger.get_logger()


# +++++++++++++++++++++++++ send_message ++++++++++++++++++++++++++++++++#

def send_message(message, peer, step, succedent_message=None):
    bot = dispatcher.bot
    kwargs = {"user_peer": peer, "step_name": step, "succedent_message": succedent_message,
              "message": message, "attempt": 1, "bot": bot}
    bot.send_message(message=message, peer=peer, success_callback=step_success, failure_callback=step_failure,
                     kwargs=kwargs)


# ++++++++++++++++++++++++++++++++++ start_bot ++++++++++++++++++++++++++++ #
@dispatcher.message_handler(
    [TemplateResponseFilter(BotButtons.back_to_main_menu), TextFilter(["/start", BotMessages.back_to_main_menu])])
def start_bot_for_users_that_do_not_logged_in(bot, update):
    user_peer = update.get_effective_user()
    was_logged = user_was_logged(user_id=user_peer.peer_id)

    if was_logged:
        start_bot_for_logged_in_users(bot, update)
    else:
        buttons_list = [BotButtons.register, BotButtons.help]
        template_message = TemplateMessage(TextMessage(BotMessages.welcome_message), buttons_list)
        send_message(message=template_message, peer=user_peer, step=Step.start_bot_for_users_that_do_not_logged_in)
        dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
            MessageHandler(filters=[TemplateResponseFilter(keywords=[BotButtons.register.value])], callback=register),
            MessageHandler(filters=[TemplateResponseFilter(keywords=BotButtons.help.value)], callback=usage_help)
        ])


common_handlers = [
    CommandHandler(commands=["/start"], callback=start_bot_for_users_that_do_not_logged_in),
    MessageHandler(TemplateResponseFilter(BotButtons.back_to_main_menu.value),
                   callback=start_bot_for_users_that_do_not_logged_in)
]


def usage_help(bot, update):
    user_peer = update.get_effective_user()
    buttons_list = [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(general_message=TextMessage(BotMessages.help_message), btn_list=buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.help)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers)


def register(bot, update):
    user_peer = update.get_effective_user()
    buttons_list = [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotMessages.enter_your_name), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.register)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), get_name_from_user),
    ])


def get_name_from_user(bot, update):
    user_peer = update.get_effective_user()
    user_name = update.get_effective_message().text
    user_id = user_peer.peer_id
    access_hash = user_peer.access_hash
    add_user_to_bot(user_name=user_name, user_id=user_id, access_hash=access_hash)
    start_bot_for_logged_in_users(bot, update)


def start_bot_for_logged_in_users(bot, update):
    user_peer = update.get_effective_user()
    buttons_list = [BotButtons.remittance, BotButtons.help]
    template_message = TemplateMessage(TextMessage(BotMessages.choose_one_option), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.start_bot_for_logged_in_users)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TemplateResponseFilter(BotButtons.remittance.value), start_remittance_conversation),
        MessageHandler(TemplateResponseFilter(BotButtons.help.value), usage_help)
    ])


def start_remittance_conversation(bot, update):
    user_peer = update.get_effective_user()
    buttons_list = [BotButtons.money_changer, BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotMessages.choose_one_money_changer), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.start_resistance_conversation)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TemplateResponseFilter(BotButtons.money_changer.value), get_receiver_name_step1)
    ])


def get_receiver_name_step1(bot, update):
    user_peer = update.get_effective_user()
    buttons_list = [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotMessages.inter_receiver_name), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.start_resistance_conversation)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), get_receiver_name_step2)
    ])


def get_receiver_name_step2(bot, update):
    user_peer = update.get_effective_user()
    receiver_name = update.get_effective_message().text
    dispatcher.set_conversation_data(update, key="receiver_name", value=receiver_name)
    buttons_list = BotButtons.cities + [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotMessages.inter_citY_name), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.get_receiver_name)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), get_city_name),
        MessageHandler(TemplateResponseFilter(keywords=[city.value for city in BotButtons.cities]), get_city_name)
    ])


def get_city_name(bot, update):
    user_peer = update.get_effective_user()
    city_name = update.get_effective_message()
    if isinstance(city_name, TextMessage):
        city_name = update.get_effective_message().text
    elif isinstance(city_name, TemplateResponseMessage):
        city_name = city_name.text_message
    dispatcher.set_conversation_data(update, key="city_name", value=city_name)
    buttons_list = [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotMessages.inter_amount), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.get_city_name)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), get_payment_amount)
    ])


def get_payment_amount(bot, update):
    user_peer = update.get_effective_user()
    amount = update.get_effective_message().text
    if amount.isnumeric():
        dispatcher.set_conversation_data(update, key="amount", value=amount)
        owner_user_id = user_peer.peer_id
        receiver_name = dispatcher.get_conversation_data(update, "receiver_name")
        city_name = dispatcher.get_conversation_data(update, "city_name")
        photo_message = BotMessages.money_request_photo_message
        owner = get_owner_with_user_id(owner_user_id)
        afghan_currency_amount = eng_to_arabic_number(
            thousand_separator(int(change_rial_to_afghan_currency(rial=int(amount), currency=140))))

        message_id = generate_random_number_with_N_digits(6)
        while message_id_is_repetitive(message_id):
            message_id = generate_random_number_with_N_digits(6)

        add_payment_to_db(owner_user_id=owner_user_id, receiver_name=receiver_name, city_name=city_name, amount=amount,
                          message_id=message_id)
        amount_message = eng_to_arabic_number(thousand_separator(amount))

        photo_message.caption_text = TextMessage(
            BotMessages.money_request_caption.format(eng_to_arabic_number(message_id), owner.name, receiver_name,
                                                     city_name, amount_message,
                                                     eng_to_arabic_number(afghan_currency_amount)))

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
        template_message = TemplateMessage(TextMessage(BotMessages.invalid_input), [BotButtons.back_to_main_menu])
        send_message(message=template_message, peer=user_peer, step=Step.get_payment_amount)
        dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
            MessageHandler(TextFilter(), get_payment_amount)
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
            BotMessages.report_message.format(payment.receiver_name, payment.destination_city_name,
                                              eng_to_arabic_number(message_id),
                                              afghan_amount, money_amount,
                                              BotMessages.payment_date))
        update_payment_is_done(message_id)
        print(report_message.text)

        send_message(report_message, money_changer, Step.send_report)
        send_message(report_message, owner_user, Step.send_report)
        send_message(report_message, muhammad, Step.send_report)
        dispatcher.register_conversation_next_step_handler(update, handlers=[
                                                                                MessageHandler(TextFilter(
                                                                                    BotMessages.back_to_main_menu),
                                                                                    start_bot_for_logged_in_users)
                                                                            ] + common_handlers)
