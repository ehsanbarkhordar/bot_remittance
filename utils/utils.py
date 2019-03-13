from random import randint
from balebot.models.messages import TemplateMessageButton

from configs import BotConfig
from constant.templates import BotTexts
from database.models import MoneyChangerBranch, MoneyChanger


def generate_random_number(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def change_rial_to_afghan_currency(rial: int, dollar_rial: float, dollar_afghani: float, remittance_fee_percent: float):
    rial_afghani = dollar_afghani / dollar_rial
    afghani = rial * rial_afghani
    afghani_fee = afghani * (remittance_fee_percent / 100)
    return afghani - afghani_fee


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
    return str('{0:,}'.format(number))


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


def get_template_buttons_from_branches(branches):
    btn_list = []
    keywords = []
    for branch in branches:
        if isinstance(branch, MoneyChangerBranch):
            keywords.append(str(branch.id))
            btn_list.append(TemplateMessageButton(text=branch.address[:60], value=branch.id, action=0))
    return btn_list, keywords


def calculate_remittance_rate(remittance_fee_percent):
    remittance_rate = int(remittance_fee_percent / 100 * 1000000)
    return remittance_rate


def get_buttons_from_money_changers(money_changers):
    btn_list = []
    keywords = []
    for changer in money_changers:
        if isinstance(changer, MoneyChanger):
            keywords.append(str(changer.id))
            remittance_rate = calculate_remittance_rate(changer.remittance_fee_percent)
            remittance_wage_for_one_million = eng_to_arabic_number(str(thousand_separator(remittance_rate)))
            text = changer.name + "/ " + BotTexts.wage.format(remittance_wage_for_one_million)
            btn_list.append(TemplateMessageButton(text=text, value=changer.id, action=0))
    return btn_list, keywords


def get_province_set_from_branches(branches):
    provinces = []
    for branch in branches:
        provinces.append(branch.province)
    provinces_set = sorted(set(provinces), key=provinces.index)
    return provinces_set


def get_branches_text(branches, province):
    keywords = []
    text = ""
    for idx, branch in enumerate(branches):
        if isinstance(branch, MoneyChangerBranch) and branch.province == province:
            branch_id = str(branch.id)
            keywords.append(branch_id)
            text += BotTexts.money_changer_branch.format(address=branch.address, branch_id=branch_id)
            text += BotTexts.fence
    return text, keywords


def get_branch_with_branch_id(branches, branch_id):
    for branch in branches:
        if branch.id == int(branch_id):
            return branch
