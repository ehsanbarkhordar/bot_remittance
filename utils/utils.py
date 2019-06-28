import csv
import os
from random import randint

from balebot.models.base_models import UserPeer
from balebot.models.messages import TemplateMessageButton

from configs import BotConfig
from constant.templates import BotTexts
from database.models import MoneyChangerBranch, MoneyChanger, PaymentRequest


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
    admin_list = get_admin_peers()
    for admin in admin_list:
        if peer_id == admin.peer_id:
            return True
    return False


def get_admin_peers():
    admin_list = []
    admins = BotConfig.admin_list.split('#')
    for admin in admins:
        admin_user_id = admin.split('*')[0]
        admin_access_hash = admin.split('*')[1]
        admin_peer = UserPeer(admin_user_id, admin_access_hash)
        admin_list.append(admin_peer)
    return admin_list


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
            dollar_rial = float(changer.dollar_rial)
            dollar_afghani = float(changer.dollar_afghani)
            afghani = change_rial_to_afghan_currency(rial=int(10000000),
                                                     dollar_rial=dollar_rial,
                                                     dollar_afghani=dollar_afghani,
                                                     remittance_fee_percent=changer.remittance_fee_percent)
            afghan_currency_amount = eng_to_arabic_number(thousand_separator(int(afghani)))
            text = changer.name + "/ " + BotTexts.wage.format(afghan_currency_amount)
            btn_list.append(TemplateMessageButton(text=text, value=changer.id, action=0))
            keywords.append(str(changer.id))

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


def create_excel(records):
    file_path = 'mydump.csv'
    outfile = open(file_path, 'w')
    outcsv = csv.writer(outfile)
    [outcsv.writerow([getattr(curr, column.name) for column in PaymentRequest.__mapper__.columns]) for curr in records]
    outfile.close()
    with open(file_path, 'rb') as f:
        f_bytes = f.read()
        os.remove(file_path)
        return f_bytes
