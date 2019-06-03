from bot.remittance_bot import updater
from database.models import MoneyChanger, MoneyChangerBranch
from database.operations import create_all_table, insert_to_table, engine


def insert_new_data():
    pass
    # obj_list = [
    #     MoneyChanger("1330762874", "برادران جعفری", "6037997503351810", 12500, 74, 1, '4525031077143068863'),
    #     MoneyChangerBranch(1, "مزار شریف", "کفایت مارکیت منزل زیر زمیان دکان۲۲، خدمات پولی برادران جعفری - محمدعلی"),
    #     MoneyChangerBranch(1, "کابل", "شعبه۱: سرای شهزاده منزل سوم، دکان۲۱۴، صرافی برادران جعفری - محمد جعفری"),
    #     MoneyChangerBranch(1, "کابل", "شعبه۲:  کابل - پلسوخته - مارکیت محمدی، منزل دوم،"
    #                                   " دکان ۷۰ سیدعلی - صرافی و خدمات پولی برادران جعفری"),
    #     MoneyChangerBranch(1, "هرات", "خراسان مارکیت: منزل تحتانی، دکان۳۳۴ صرافی برادران جعفری؛ محمد"),
    # ]
    # insert_to_table(obj_list)
    # obj_list = [
    #     MoneyChanger("1625735178", "ملا فضل‌الدین ایوبی", "6037697460825448", 12500, 74, 1, '5373262855830733382'),
    #     MoneyChangerBranch(2, "مزار شریف", "غرب روضه مبارک، کفایت مارکیت، منزل ۴، اتاق ۴۰۸، صرافی ملا محمد"),
    #     MoneyChangerBranch(2, "کابل", "سینمای پامیر، جاده میوند، حیدری مارکیت، منزل اول، اتاق ۱۳۷، صرافی ضیاءالحق"),
    # ]
    # insert_to_table(obj_list)
    # insert_to_table([
    #     MoneyChanger("1625735178", "ملا محمد صراف", "6037697460825448", 12500, 74, 1),
    #     MoneyChangerBranch(2, "سرپل", "سرپل؛ شهر نو؛ دکان ملا محمد صراف"),
    # ])
    # insert_to_table(MoneyChangerBranch(1, "بامیان", "بامیان؛ زیر هتل ستاره شهر؛ صرافی برادران جعفری"))


if __name__ == '__main__':
    updater.run()
