from random import randint


def generate_random_number_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def change_rial_to_afghan_currency(rial, currency):
    toman = int(rial) / 10
    afghan = toman / currency
    return afghan


def eng_to_arabic_number(number):
    number = str(number)
    return number.translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹'))


def thousand_separator(number):
    number = int(number)
    return '{0:,}'.format(number)
