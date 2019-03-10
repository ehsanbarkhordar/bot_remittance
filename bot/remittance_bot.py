import asyncio

from balebot.filters import TemplateResponseFilter, TextFilter, DefaultFilter, BankMessageFilter
from balebot.handlers import MessageHandler, CommandHandler
from balebot.models.messages import TemplateMessage, TextMessage, PurchaseMessage, BankMessage
from balebot.models.messages.banking.money_request_type import MoneyRequestType
from balebot.updater import Updater

from configs import BotConfig
from constant.templates import BotButtons, Step, BotMessages, Patterns
from bot.call_backs import step_success, step_failure
from balebot.utils.logger import Logger

from database.models import PaymentRequest
from database.operations import select_all_province_names, update_money_changer_remittance_fee_percent, \
    select_money_changer_by_peer_id, update_money_changer_dollar_rial, \
    update_money_changer_card_number, update_money_changer_dollar_afghani, insert_to_table, \
    select_branches_by_money_changer_id, delete_from_table, select_money_changers, select_money_changer_by_id, \
    select_last_payment_request
from utils.utils import *

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


@dispatcher.message_handler(DefaultFilter())
def start(bot, update):
    user_peer = update.get_effective_user()
    money_changer = select_money_changer_by_peer_id(user_peer.peer_id)
    if money_changer and isinstance(money_changer, MoneyChanger):
        money_changer_panel(bot, update)
    else:
        user_panel(bot, update)


@dispatcher.message_handler(TemplateResponseFilter([BotButtons.help.value]))
def help_me(bot, update):
    user_peer = update.get_effective_user()
    buttons_list = [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(general_message=TextMessage(BotTexts.help_message), btn_list=buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.help)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers)


# @dispatcher.message_handler(TemplateResponseFilter([BotButtons.user_panel.value]))
def user_panel(bot, update):
    user_peer = update.get_effective_user()
    buttons_list = [BotButtons.remittance, BotButtons.help]
    template_message = TemplateMessage(TextMessage(BotTexts.choose_one_option), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.user_panel)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TemplateResponseFilter(BotButtons.remittance.value), request_sender_name),
        MessageHandler(TemplateResponseFilter(BotButtons.help.value), help_me)
    ])


def request_sender_name(bot, update):
    user_peer = update.get_effective_user()
    text_message = TextMessage(BotTexts.enter_sender_name)
    send_message(message=text_message, peer=user_peer, step=Step.request_sender_name)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), request_money_changer),
    ])


# def request_sender_father_name(bot, update):
#     user_peer = update.get_effective_user()
#     sender_name = update.get_effective_message().text
#     dispatcher.set_conversation_data(update, key="sender_name", value=sender_name)
#     text_message = TextMessage(BotTexts.enter_sender_father_name)
#     send_message(message=text_message, peer=user_peer, step=Step.request_sender_father_name)
#     dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
#         MessageHandler(TextFilter(), request_money_changer),
#     ])


def request_money_changer(bot, update):
    user_peer = update.get_effective_user()
    sender_name = update.get_effective_message().text
    dispatcher.set_conversation_data(update, key="sender_name", value=sender_name)
    money_changers = select_money_changers()
    buttons_list, keywords = get_buttons_from_money_changers(money_changers)
    if buttons_list:
        buttons_list += [BotButtons.back_to_main_menu]
        template_message = TemplateMessage(TextMessage(BotTexts.choose_one_money_changer), buttons_list)
        send_message(message=template_message, peer=user_peer, step=Step.request_money_changer)
        dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
            MessageHandler(TemplateResponseFilter(keywords=keywords), request_province)
        ])
    else:
        buttons_list += [BotButtons.back_to_main_menu]
        template_message = TemplateMessage(TextMessage(BotTexts.no_money_changer_found), buttons_list)
        send_message(message=template_message, peer=user_peer, step=Step.request_money_changer)
        dispatcher.finish_conversation(update)


def request_province(bot, update):
    user_peer = update.get_effective_user()
    money_changer_id = update.get_effective_message().text
    money_changer = select_money_changer_by_id(money_changer_id)
    dispatcher.set_conversation_data(update, "money_changer", money_changer)
    branches = select_branches_by_money_changer_id(money_changer.id)
    province_set = get_province_set_from_branches(branches)
    dispatcher.set_conversation_data(update, "branches", branches)
    province_buttons = get_template_buttons_from_list(province_set)
    buttons_list = province_buttons + [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotTexts.choose_province), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.request_province)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TemplateResponseFilter(keywords=province_set), request_branch)
    ])


def request_branch(bot, update):
    user_peer = update.get_effective_user()
    province = update.get_effective_message().text
    dispatcher.set_conversation_data(update, "province", province)
    branches = dispatcher.get_conversation_data(update, "branches")
    branches_text, keywords = get_branches_text(branches, province)
    buttons_list = [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(branches_text), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.request_branch)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(keywords=keywords), request_receiver_name),
    ])


def request_receiver_name(bot, update):
    user_peer = update.get_effective_user()
    branch_id = update.get_effective_message().text
    dispatcher.set_conversation_data(update, key="branch_id", value=branch_id)
    buttons_list = [BotButtons.back_to_main_menu]
    general_message = TextMessage(BotTexts.enter_receiver_name)
    template_message = TemplateMessage(general_message, buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.request_receiver_name)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), request_receiver_father_name)
    ])


def request_receiver_father_name(bot, update):
    user_peer = update.get_effective_user()
    receiver_name = update.get_effective_message().text
    dispatcher.set_conversation_data(update, key="receiver_name", value=receiver_name)
    buttons_list = [BotButtons.back_to_main_menu]
    general_message = TextMessage(BotTexts.enter_receiver_father_name)
    template_message = TemplateMessage(general_message, buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.request_receiver_father_name)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), request_amount)
    ])


def request_amount(bot, update):
    user_peer = update.get_effective_user()
    receiver_father_name = update.get_effective_message().text
    dispatcher.set_conversation_data(update, key="receiver_father_name", value=receiver_father_name)
    buttons_list = [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotTexts.enter_amount), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.request_amount)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), get_amount)
    ])


def get_amount(bot, update):
    user_peer = update.get_effective_user()
    amount = update.get_effective_message().text
    if amount.isnumeric():
        dispatcher.set_conversation_data(update, "remittance_amount", amount)
        send_payment_message(bot, update)
    else:
        template_message = TemplateMessage(TextMessage(BotTexts.invalid_amount), [BotButtons.back_to_main_menu])
        send_message(message=template_message, peer=user_peer, step=Step.get_payment_amount)
        dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
            MessageHandler(TextFilter(), get_amount)
        ])


def send_payment_message(bot, update):
    user_peer = update.get_effective_user()
    remittance_amount = dispatcher.get_conversation_data(update, "remittance_amount")
    receiver_name = dispatcher.get_conversation_data(update, "receiver_name")
    receiver_father_name = dispatcher.get_conversation_data(update, "receiver_father_name")
    sender_name = dispatcher.get_conversation_data(update, "sender_name")
    branch_id = dispatcher.get_conversation_data(update, "branch_id")
    branches = dispatcher.get_conversation_data(update, "branches")
    province = dispatcher.get_conversation_data(update, "province")
    money_changer = dispatcher.get_conversation_data(update, "money_changer")

    branch = get_branch_with_branch_id(branches, branch_id)

    photo_message = BotMessages.money_request_photo_message
    dollar_rial = float(money_changer.dollar_rial)
    dollar_afghani = float(money_changer.dollar_afghani)
    afghani = change_rial_to_afghan_currency(rial=int(remittance_amount),
                                             dollar_rial=dollar_rial,
                                             dollar_afghani=dollar_afghani)
    afghan_currency_amount = thousand_separator(int(afghani))
    last_payment_request = select_last_payment_request()
    if last_payment_request:
        last_payment_request_id = last_payment_request.id
    else:
        last_payment_request_id = 1
    message_id = "B" + str(1000 + last_payment_request_id)
    amount_message = thousand_separator(remittance_amount)
    money_request_caption = BotTexts.money_request_caption.format(
        message_id, sender_name, receiver_name, receiver_father_name,
        branch.province, branch.address, amount_message,
        afghan_currency_amount)
    money_request_caption = eng_to_arabic_number(money_request_caption)

    photo_message.caption_text = TextMessage(money_request_caption)
    logger.info("success send payment request" + "account_number: {}, amount: {}".format(money_changer.card_number,
                                                                                         remittance_amount))
    purchase_message = PurchaseMessage(account_number=money_changer.card_number, amount=int(remittance_amount),
                                       money_request_type=MoneyRequestType.normal, msg=photo_message)
    send_message(message=purchase_message, peer=user_peer, step=Step.send_payment_message)
    payment_request = PaymentRequest(message_id=message_id, payer_peer_id=user_peer.peer_id,
                                     money_changer_peer_id=money_changer.peer_id, sender_name=sender_name,
                                     receiver_name=receiver_name + "-" + receiver_father_name, province=province,
                                     money_changer_branch_id=int(branch_id), remittance_amount=int(remittance_amount))
    insert_to_table(payment_request)
    dispatcher.finish_conversation(update)


# @dispatcher.message_handler(BankMessageFilter())
# def send_report(bot, update):
#     # update = test_update_2
#     message = update.get_effective_message()
#     user_peer = update.get_effective_user()
#     user_id = user_peer.peer_id
#     if isinstance(message, BankMessage) and int(user_id) == 11:
#         receipt = message.get_receipt()
#         message_id = receipt.regarding.splitlines()[0]
#         print(message_id)
#         message_id = int(re.search(r'\d+', message_id).group())
#         print(message_id)
#         payment = get_payment_with_message_id(message_id)
#         owner = payment.owner
#         owner_user = UserPeer(peer_id=owner.user_id, access_hash=owner.access_hash)
#         money_changer_user_id = 776725385
#         money_changer_access_hash = "-3564513944394449112"
#         muhammad_user_id = 1314892980
#         muhammad_access_hash = "6115941441665528566"
#         money_changer = UserPeer(peer_id=money_changer_user_id, access_hash=money_changer_access_hash)
#         muhammad = UserPeer(peer_id=muhammad_user_id, access_hash=muhammad_access_hash)
#
#         afghan_amount = eng_to_arabic_number(int(change_rial_to_afghan_currency(int(payment.money_amount), 140)))
#         money_amount = eng_to_arabic_number(thousand_separator(payment.money_amount))
#         report_message = TextMessage(
#             BotTexts.report_message.format(payment.receiver_name, payment.destination_city_name,
#                                            eng_to_arabic_number(message_id),
#                                            afghan_amount, money_amount,
#                                            BotTexts.payment_date))
#         update_payment_is_done(message_id)
#         print(report_message.text)
#
#         send_message(report_message, money_changer, Step.send_report)
#         send_message(report_message, owner_user, Step.send_report)
#         send_message(report_message, muhammad, Step.send_report)
#         dispatcher.register_conversation_next_step_handler(update, handlers=[
#                                                                                 MessageHandler(TextFilter(
#                                                                                     BotTexts.back_to_main_menu),
#                                                                                     user_panel)
#                                                                             ] + common_handlers)
#

# +++++++++++++++++++++++++++++++++++++++ Money Changer Panel ++++++++++++++++++++++++++++++++++++++++++++++++
# @dispatcher.message_handler(TemplateResponseFilter([BotButtons.money_changer_panel.value]))
def money_changer_panel(bot, update):
    user_peer = update.get_effective_user()

    money_changer = select_money_changer_by_peer_id(user_peer.peer_id)
    buttons_list = [BotButtons.register_branch, BotButtons.update_card_number, BotButtons.update_dollar_rial,
                    BotButtons.update_dollar_afghani, BotButtons.update_remittance_fee_percent,
                    BotButtons.remove_branch, BotButtons.help]
    dollar_rial = money_changer.dollar_rial
    remittance_fee_percent = money_changer.remittance_fee_percent
    dollar_afghani = money_changer.dollar_afghani
    if not money_changer.dollar_rial:
        dollar_rial = BotTexts.undefined
    if not money_changer.dollar_afghani:
        dollar_afghani = BotTexts.undefined
    if not money_changer.remittance_fee_percent:
        remittance_fee_percent = BotTexts.undefined
    text = BotTexts.money_changer_info.format(money_changer.name, money_changer.card_number,
                                              dollar_rial, dollar_afghani, remittance_fee_percent)
    text = eng_to_arabic_number(text)
    text += BotTexts.choose_one_option
    template_message = TemplateMessage(TextMessage(text), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.start_bot_for_logged_in_users)
    dispatcher.finish_conversation(update)


# +++++++++++++++++++++++++++++++++++++++ Add New Branch ++++++++++++++++++++++++++++++++++++++++++++++++
@dispatcher.message_handler(TemplateResponseFilter(BotButtons.register_branch.value))
def request_province_name(bot, update):
    user_peer = update.get_effective_user()
    province_names = select_all_province_names()
    province_name_buttons = get_template_buttons_from_list(province_names)
    template_message = TemplateMessage(TextMessage(BotTexts.choose_or_enter_province), province_name_buttons)
    send_message(message=template_message, peer=user_peer, step=Step.request_province_name)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TemplateResponseFilter(keywords=province_names), request_branch_address),
        MessageHandler(TextFilter(), request_branch_address)])


def request_branch_address(bot, update):
    user_peer = update.get_effective_user()
    province = update.get_effective_message().text
    dispatcher.set_conversation_data(update, "province", province)
    text_message = TextMessage(BotTexts.enter_branch_address)
    send_message(message=text_message, peer=user_peer, step=Step.request_branch_address)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(), insert_branch)])


def insert_branch(bot, update):
    user_peer = update.get_effective_user()
    address = update.get_effective_message().text
    province = dispatcher.get_conversation_data(update, "province")
    money_changer = select_money_changer_by_peer_id(user_peer.peer_id)
    table_object = MoneyChangerBranch(money_changer_id=money_changer.id, address=address, province=province)
    res = insert_to_table(table_object)
    buttons_list = [BotButtons.back_to_main_menu]
    if res:
        text_message = TextMessage(BotTexts.branch_inserted_successfully)
    else:
        text_message = TextMessage(BotTexts.error)
    template_message = TemplateMessage(text_message, buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.insert_branch)
    dispatcher.finish_conversation(update)


# +++++++++++++++++++++++++++++++++++++++ Remove Branch ++++++++++++++++++++++++++++++++++++++++++++++++
@dispatcher.message_handler(TemplateResponseFilter(BotButtons.remove_branch.value))
def show_current_money_branches(bot, update):
    user_peer = update.get_effective_user()
    money_changer = select_money_changer_by_peer_id(user_peer.peer_id)
    branches = select_branches_by_money_changer_id(money_changer_id=money_changer.id)
    dispatcher.set_conversation_data(update, "branches", branches)
    if branches:
        branches_buttons, keywords = get_template_buttons_from_branches(branches)
        template_message = TemplateMessage(TextMessage(BotTexts.choose_branch_for_remove), branches_buttons)
        send_message(message=template_message, peer=user_peer, step=Step.request_province_name)
        dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
            MessageHandler(TemplateResponseFilter(keywords=keywords), remove_money_branch)])
    else:
        buttons_list = [BotButtons.back_to_main_menu]
        template_message = TemplateMessage(TextMessage(BotTexts.no_branches_found), buttons_list)
        send_message(message=template_message, peer=user_peer, step=Step.request_province_name)
        dispatcher.finish_conversation(update)


def remove_money_branch(bot, update):
    user_peer = update.get_effective_user()
    branch_id = update.get_effective_message().text
    branches = dispatcher.get_conversation_data(update, "branches")
    for branch in branches:
        if branch.id == int(branch_id):
            res = delete_from_table(table_object=branch)
            if res:
                buttons_list = [BotButtons.back_to_main_menu]
                template_message = TemplateMessage(TextMessage(BotTexts.branch_deleted_successfully), buttons_list)
                send_message(message=template_message, peer=user_peer, step=Step.request_province_name)
                dispatcher.finish_conversation(update)
                return 0
    buttons_list = [BotButtons.back_to_main_menu]
    template_message = TemplateMessage(TextMessage(BotTexts.no_branches_found), buttons_list)
    send_message(message=template_message, peer=user_peer, step=Step.request_province_name)
    dispatcher.finish_conversation(update)


# ++++++++++++++++++++++++++++++++++ Update Money Changer Info ++++++++++++++++++++++++++++++++
@dispatcher.message_handler(TemplateResponseFilter(BotButtons.update_remittance_fee_percent.value))
def request_remittance_fee_percent(bot, update):
    user_peer = update.get_effective_user()
    text_message = TextMessage(BotTexts.enter_new_remittance_fee_percent)
    dispatcher.set_conversation_data(update, "previous_state", request_remittance_fee_percent)
    send_message(message=text_message, peer=user_peer, step=Step.request_remittance_fee_percent)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(pattern=Patterns.number_only), update_money_changer),
    ])


@dispatcher.message_handler(TemplateResponseFilter(BotButtons.update_dollar_rial.value))
def request_dollar_rial(bot, update):
    user_peer = update.get_effective_user()
    text_message = TextMessage(BotTexts.enter_new_dollar_rial)
    dispatcher.set_conversation_data(update, "previous_state", request_dollar_rial)
    send_message(message=text_message, peer=user_peer, step=Step.request_dollar_rial)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(pattern=Patterns.float_numbers), update_money_changer),
    ])


@dispatcher.message_handler(TemplateResponseFilter(BotButtons.update_dollar_afghani.value))
def request_dollar_afghani(bot, update):
    user_peer = update.get_effective_user()
    text_message = TextMessage(BotTexts.enter_new_dollar_afghani)
    dispatcher.set_conversation_data(update, "previous_state", request_dollar_afghani)
    send_message(message=text_message, peer=user_peer, step=Step.request_dollar_afghani)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(pattern=Patterns.float_numbers), update_money_changer),
    ])


@dispatcher.message_handler(TemplateResponseFilter(BotButtons.update_card_number.value))
def request_card_number(bot, update):
    user_peer = update.get_effective_user()
    text_message = TextMessage(BotTexts.enter_new_card_number)
    dispatcher.set_conversation_data(update, "previous_state", request_card_number)
    send_message(message=text_message, peer=user_peer, step=Step.request_card_number)
    dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
        MessageHandler(TextFilter(pattern=Patterns.float_numbers), update_money_changer),
    ])


def update_money_changer(bot, update):
    user_peer = update.get_effective_user()
    text_entered = arabic_to_eng_number(update.get_effective_message().text)
    previous_state = dispatcher.get_conversation_data(update, "previous_state")
    money_changer = select_money_changer_by_peer_id(user_peer.peer_id)
    res = None
    text_message = None
    if previous_state == request_remittance_fee_percent:
        percent = float(text_entered)
        res = update_money_changer_remittance_fee_percent(money_changer=money_changer, percent=percent)
        text_message = TextMessage(BotTexts.remittance_fee_percent_updated_successfully.format(percent))
    elif previous_state == request_dollar_rial:
        dollar_rial = float(text_entered)
        res = update_money_changer_dollar_rial(money_changer=money_changer, dollar_rial=dollar_rial)
        text_message = TextMessage(BotTexts.dollar_rial_updated_successfully.format(dollar_rial))
    elif previous_state == request_dollar_afghani:
        dollar_afghani = float(text_entered)
        res = update_money_changer_dollar_afghani(money_changer=money_changer, dollar_afghani=dollar_afghani)
        text_message = TextMessage(BotTexts.dollar_afghani_updated_successfully.format(dollar_afghani))
    elif previous_state == request_card_number:
        card_number = text_entered
        res = update_money_changer_card_number(money_changer=money_changer, card_number=card_number)
        text_message = TextMessage(BotTexts.card_number_updated_successfully.format(card_number))
    if res:
        buttons_list = [BotButtons.back_to_main_menu]
        template_message = TemplateMessage(text_message, buttons_list)
        send_message(message=template_message, peer=user_peer, step=Step.update_money_changer)
        dispatcher.register_conversation_next_step_handler(update, handlers=common_handlers + [
            MessageHandler(TextFilter(Patterns.float_numbers), request_sender_name)])
    else:
        buttons_list = [BotButtons.back_to_main_menu]
        template_message = TemplateMessage(TextMessage(BotTexts.error), buttons_list)
        send_message(message=template_message, peer=user_peer, step=Step.update_money_changer)
        dispatcher.finish_conversation(update)


# +++++++++++++++++++++++++++++ COMMON HANDLERS ++++++++++++++++++++++++++++++
common_handlers = [
    CommandHandler(commands=["/start"], callback=start),
    CommandHandler(commands=["/help"], callback=help_me),
    MessageHandler(TemplateResponseFilter(keywords=[BotButtons.help.value]), callback=help_me),
    MessageHandler(TemplateResponseFilter(keywords=[BotButtons.back_to_main_menu.value]), callback=start)
]
