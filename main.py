from bot.remittance_bot import updater
from database.models import MoneyChanger, MoneyChangerBranch
from database.operations import create_all_table, insert_to_table, delete_all_table


def insert_mock_data():
    obj_list = [
        MoneyChanger("201707397", "برادران جعفری", "6037997473091040", 12500, 74, 1),
        MoneyChanger("1417824523", "برادران حسن نژاد", "6037997473091040", 13500, 75, 2),

        MoneyChangerBranch(1, "مزار شریف", "کفایت مارکیت منزل زیر زمیان دکان ۲۲،خدمات پولی برادران جعفری- محمدعلی"),
        MoneyChangerBranch(1, "کابل", "شعبه 1 : سرای شهزاده منزل سوم، دکان ۲۱۴،صرافی برادران جعفری -محمد جعفری"),
        MoneyChangerBranch(1, "کابل", "شعبه 2 :  کابل-پلسوخته -مارکیت محمدی، منزل دوم،"
                                      " دکان 70 سیدعلی-صرافی و خدمات پولی برادران جعفری"),
        MoneyChangerBranch(1, "هرات", "خراسان مارکیت: منزل تحتانی،دکان 334 صرافی برادران جعفری؛ محمد"),
    ]
    insert_to_table(obj_list)




if __name__ == '__main__':
    # delete_all_table()
    # create_all_table()
    # insert_mock_data()
    updater.run()
