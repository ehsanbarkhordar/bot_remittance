from bot.remittance_bot import updater
from database.models import MoneyChanger, MoneyChangerBranch
from database.operations import create_all_table, insert_to_table, drop_all_table, engine


def insert_mock_data():
    obj_list = [
        MoneyChanger("201707397", "برادران جعفری", "6037997503351810", 12500, 74, 1),
        MoneyChangerBranch(1, "مزار شریف", "کفایت مارکیت منزل زیر زمیان دکان۲۲، خدمات پولی برادران جعفری - محمدعلی"),
        MoneyChangerBranch(1, "کابل", "شعبه۱: سرای شهزاده منزل سوم، دکان۲۱۴، صرافی برادران جعفری - محمد جعفری"),
        MoneyChangerBranch(1, "کابل", "شعبه ۲:  کابل - پلسوخته - مارکیت محمدی، منزل دوم،"
                                      " دکان ۷۰ سیدعلی - صرافی و خدمات پولی برادران جعفری"),
        MoneyChangerBranch(1, "هرات", "خراسان مارکیت: منزل تحتانی، دکان۳۳۴ صرافی برادران جعفری؛ محمد"),
    ]
    insert_to_table(obj_list)


if __name__ == '__main__':
    if not engine.dialect.has_table(engine, MoneyChanger.__tablename__):  # If table don't exist, Create.
        drop_all_table()
        create_all_table()
        insert_mock_data()
    updater.run()
