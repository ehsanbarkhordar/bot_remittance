from random import randint

from balebot.config import Config
from balebot.models.messages import TemplateMessageButton

from configs import BotConfig


def generate_random_number_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def change_rial_to_afghan_currency(rial, currency):
    toman = int(rial) / 10
    afghan = toman / currency
    return afghan


def arabic_to_eng_number(number):
    if isinstance(number, str):
        return number.translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩', '01234567890123456789'))
    elif isinstance(number, list):
        return [str(num).translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩', '01234567890123456789')) for num in number]


def eng_to_arabic_number(number):
    if isinstance(number, str):
        return number.translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹'))
    elif isinstance(number, list):
        return [str(num).translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')) for num in number]


def thousand_separator(number):
    number = int(number)
    return '{0:,}'.format(number)


def is_admin(peer_id):
    admin_list = BotConfig.admin_list
    admin_list = admin_list.split("-")
    if peer_id in admin_list:
        return True
    else:
        return False


def get_template_buttons_from_list(input_list):
    btn_list = []
    for i in input_list:
        btn_list.append(TemplateMessageButton(text=i))
    return btn_list
