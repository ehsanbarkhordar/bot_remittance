from balebot.models.base_models import FatSeqUpdate
from balebot.models.messages import TemplateMessageButton, PhotoMessage, TextMessage
import jdatetime
from utils.utils import eng_to_arabic_number


class BotTexts:
    enter_sender_name = "لطفا نام پرداخت کننده را به همراه نام پدر وارد نمایید:"
    choose_one_money_changer = "لطفا صرافی موردنظر را *انتخاب* کنید:"
    back_to_main_menu = "بازگشت به منوی اصلی"
    invalid_input = "ورودی اشتباه است،\nلطفاً مبلغ را به *عدد* وارد نمایید:"
    enter_amount = "لطفاً مبلغ را به *ریال* وارد نمایید:"
    enter_city_name = "لطفاً نام *شهر محل دریافت پول* را *انتخاب* و یا *وارد* کنید: "
    enter_receiver_name = "لطفاً نام دریافت کننده پول را *وارد* نمایید:"
    choose_one_option = "لطفاً یک گزینه را *انتخاب* کنید:"
    enter_your_name = "لطفاً نام و نام خانوادگی خود را وارد نمایید:"
    welcome_message = "سلام خوش آمدید،‌ لطفاً یکی از گزینه های زیر را *انتخاب* کنید:"
    help_message = "به کمک این بازو می‌توانید مبلغ دلخواه را به فرد مورد نظر در افغانستان انتقال دهید." + "\n" \
                   + "لازم است ابتدا *ثبت نام* کنید و سپس از طریق گزینه *انتقال پول* و انتخاب *صرافی،* نرخ تبدیل ارز را ملاحظه خواهید کرد. در ادامه *نام دریافت‌کننده پول* در افغانستان، *شهر محل دریافت پول* و سپس *مبلغ* موردنظرتان را به *ریال* وارد می‌کنید." + "\n" + "در این مرحله پیام پرداخت پول را مشاهده خواهید کرد که با انتخاب گزینه پرداخت و وارد کردن اطلاعات کارت، می‌توانید مبلغ را انتقال دهید." + "\n" + "پس از این مرحله *رسید انتقال* را دریافت می‌کنید و می‌توانید رسید انتقال را برای دریافت‌کننده ارسال کنید. فرد دریافت‌‌کننده با داشتن *کد شش رقمی* می‌تواند برای گرفتن پول به صرافی مشخص شده در شهری که شما انتخاب کرده‌اید، مراجعه کند. "
    report_message = "*رسید انتقال*" + "\n" + "انتقال پول با *موفقیت* انجام شد." \
                     + "\n" + "آقا/خانم *{}* می‌تواند در " \
                              "شهر *{}* با ارائه کد *{}* " \
                              "مبلغ *{}* افغانی،معادل *{}* ریال را از صرافی " \
                              "*افضلی-صلواتی* دریافت کند." \
                     + "\n" "تاریخ انتقال: *{" \
                       "}* " + "\n" + "[بازگشت به منوی اصلی](send:بازگشت به منوی اصلی)"
    now = jdatetime.datetime.now()
    payment_date = "{}/{}/{} ساعت {}:{}".format(eng_to_arabic_number(now.year), eng_to_arabic_number(now.month),
                                                eng_to_arabic_number(now.day), eng_to_arabic_number(now.hour),
                                                eng_to_arabic_number(now.minute))
    hyper_link = "[{}](send: {})"
    select = "انتخاب"
    money_changer_mazar_address = "کفایت مارکیت منزل زیر زمیان دکان ۲۲،خدمات پولی برادران جعفری- محمدعلی"
    money_changer_mazar = "مزار شریف: {}\n" \
                          "{}".format(money_changer_mazar_address,
                                      hyper_link.format(select, money_changer_mazar_address))

    money_changer_harat_address = "خراسان مارکیت: منزل تحتانی،دکان 334 صرافی برادران جعفری؛ محمد"
    money_changer_harat = "هرات: {}\n" \
                          "{}".format(money_changer_harat_address,
                                      hyper_link.format(select, money_changer_harat_address))

    money_changer_kabol_address1 = "شعبه 1 : سرای شهزاده منزل سوم، دکان ۲۱۴،صرافی برادران جعفری -محمد جعفری"
    money_changer_kabol_address2 = "شعبه 2 :  کابل-پلسوخته -مارکیت محمدی، منزل دوم، دکان 70 سیدعلی-صرافی و خدمات پولی برادران جعفری"
    money_changer_kabol = "کابل: {}\n" \
                          "{}".format(money_changer_kabol_address1,
                                      hyper_link.format(select, money_changer_kabol_address1)) + \
                          "\n======================\n" \
                          "کابل: {}\n" \
                          "{}".format(money_changer_kabol_address2,
                                      hyper_link.format(select, money_changer_kabol_address2))

    thumb = "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAA4KCw0LCQ4NDA0QDw4RFiQXFhQUFiwgIRokNC43NjMuMjI6QVNGOj1OPjIySGJJTlZYXV5dOEVmbWVabFNbXVn/2wBDAQ8QEBYTFioXFypZOzI7WVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVn/wAARCAA0AFoDASIAAhEBAxEB/8QAGwABAQADAQEBAAAAAAAAAAAAAAUBBAYDBwL/xAA1EAACAgEDAgMGAwcFAAAAAAABAgMRAAQFIRIxIkFRBhNhcYGRFULwFCMyUqGx0UOSk9Lh/8QAGQEBAAMBAQAAAAAAAAAAAAAAAAECBAMF/8QAJhEAAgECBAUFAAAAAAAAAAAAAAECAxEEITFBEiIykfAUQlFhgf/aAAwDAQACEQMRAD8A+kYxjAGZzGZwBmpucEmp0MkUUjxuaIdGKsKIPFefwPB8+M95ZRELYGvXyHz9MkbhuOpSfTRRS6eFZpH07m+plkKhkHV2UkX3Dd14N8Abei1s0jJFqYlEhXl4zaEgC+DyLPVQ54HJs1m6ro5cKysUPSwBvpNXR+hH3z597S6fWR6yVZZNUdOaQNJ0lZPzdRCqI7Jvir8NnuMo7Hv8c7R6hkWTWamYI508QctEGKqHKnwkdQayACAQBkXzsc41FKTj8HZYxjJOgxjGAMYzOAeGrRGgLSSmFYyJC/V0ha55+HrecxuvtNqNs1U+lkjEg6Or3gkVGQEd1BB7Uf4hyb8qvpNbE0kEqkK6MvSY3W1Yc2CPOxxWQm9ntTrpk/b9Yz6aIdKofEXAJIuxfUDVNZNWO9s0MrNSa5dSvtuvG46eSaOmjVx7tlPLqVVgSPI81z6X2IyVuu1zar3gjjno14YyFdKPUCrdXStEWK5LdHV4VOWNujnh99HO1r13EoUAInSBVjvyGP1zcySxxmp9mHbRO25zJKFkV0DyNKwJ4Kq0hpbJA+JAJ8lWtsOk05jZmjdpoSEJkYEiqKqwBolRRHHHVfcsTcZQ6lWAKkUQfPNDbNBNotRrmkmSSPUSiVAqFSvhC0TZvhV9PP5AV4Ve5QxjGCwzOYzOAYyX7QQCbb3ZUImQWsqDxxgkdRQ/zV2+NZTa+k9JAauCRYyPpX3GTdpizXp0NBGAUAXQoi74s/7RfehDP1sGl1un0wbXyNJJIi0GN+7A/IfUi+/nlfGMBKysMZh3WNGd2CqossTQA9c5LcN2m3SR4tOzR6DlSappvX4gfr4DnUqRpx4pFZzUcty3rN70mlkMSltRKDTJCL6e/c9h27XeTH3/AFrspSHTwqR2cmQ39KyUGighBsJGP19883kkmUrHD4T+aQ9I+HHf+2eZPGVJdOSOTk932LH43uHrpf8Aib/tntDv2pUgTwxSAnkxkpQ+Ruz9RnOqupSZI5JyEI8JVAbPpZ8893gdhxqJARyDS8H7ZT1NWLzl52IUnsmdfo910usYIrGOU/6cnDH5eR4HkTWb2cBA0skdsUYrwVIohh6n/wAygu4a9VCrrJKAoWqH+pFn65qjjksprP6Okaja0OtJoHJPs3uM257c0+oCB/eFfAKFUP8AOMZ6B03K+MYwSc37XTP06LSX+6nclwLs9NUPlz/QZNAAAAFAdgMYzyMe+dIz++X4T9MPeGDUvzJIzA+gFHt9v75QxjMlXVeblaOhM3TUvHIIlC1QYEjkG88fxaf+SP7H/OMZohFOCujPOTU3Zmxt2peeeYsALAJAur7fr5ZRxjM9XqNFHpP/2Q=="

    money_request_caption = "کد انتقال: *{}*\nواریز کننده: *{}*\nنام دریافت کننده: *{}*\nشهر محل دریافت: *{}*\n" \
                            "آدرس صرافی: {}\n" \
                            "مبلغ: *{}* ریال معادل *{}* افغانی"

    test_update_3 = FatSeqUpdate('{"$type":"FatSeqUpdate","seq":1556,"body":{"$type":"Message","peer":{"$type":"User",'
                                 '"id":11,"accessHash":"3192746565014995892"},"sender":{"$type":"User","id":11,'
                                 '"accessHash":"3192746565014995892"},"date":"1547885026193",'
                                 '"randomId":"-2226549050919207673","message":{"$type":"BankMessage","message":{'
                                 '"$type":"ReceiptMessage","message":{"$type":"MapValue","items":[{"key":"fa",'
                                 '"value":{"$type":"StringVal","text":"<html><span><b>انتقال '
                                 'پول</b></span><br/><span>مبلغ دریافتی: </span><span><font color=\'#40d0a3\'>۱۰۰+ '
                                 'ریال</font></span><br/><span>کارت مبدا: '
                                 '</span><span>۶۰۳۷۹۹XXXXXX۷۰۷۲</span><br/><span>کارت مقصد: '
                                 '</span><span>۶۰۳۷۹۹XXXXXX۲۱۰۶</span><br/><span>صاحب کارت مقصد: </span><span>محمد '
                                 'اژدری</span><br/><span>واریزکننده: </span><span>S.shad - @sshad</span><br/><span>بابت: '
                                 '</span><span>شماره انتقال: ۱۰۰۰۲\\nواریز کننده: *محمدس*\\nنام دریافت کننده: '
                                 '*آقاکریمی*\\nشهر محل دریافت: *جنت آباد*\\nمبلغ: *۱۰۰* ریال معادل *۰* '
                                 'افغانی</span><br/><span>توضیحات: </span><span>رسید سه</span><br/><span>شماره پیگیری: '
                                 '</span><span>۱۱۳۹۲۹</span><br/><span>تاریخ انتقال: '
                                 '</span><span><date>۱۵۴۷۸۸۵۰۲۶۱۴۱</date></span><br/><span>#کارت_ب_کارت #دریافت '
                                 '#موفق</span></html>"}},{"key":"en","value":{"$type":"StringVal",'
                                 '"text":"<html><span><b>انتقال پول</b></span><br/><span>مبلغ دریافتی: </span><span><font '
                                 'color=\'#40d0a3\'>۱۰۰+ ریال</font></span><br/><span>کارت مبدا: '
                                 '</span><span>۶۰۳۷۹۹XXXXXX۷۰۷۲</span><br/><span>کارت مقصد: '
                                 '</span><span>۶۰۳۷۹۹XXXXXX۲۱۰۶</span><br/><span>صاحب کارت مقصد: </span><span>محمد '
                                 'اژدری</span><br/><span>واریزکننده: </span><span>S.shad - @sshad</span><br/><span>بابت: '
                                 '</span><span>شماره انتقال: ۱۰۰۰۲\\nواریز کننده: *محمدس*\\nنام دریافت کننده: '
                                 '*آقاکریمی*\\nشهر محل دریافت: *جنت آباد*\\nمبلغ: *۱۰۰* ریال معادل *۰* '
                                 'افغانی</span><br/><span>توضیحات: </span><span>رسید سه</span><br/><span>شماره پیگیری: '
                                 '</span><span>۱۱۳۹۲۹</span><br/><span>تاریخ انتقال: '
                                 '</span><span><date>۱۵۴۷۸۸۵۰۲۶۱۴۱</date></span><br/><span>#کارت_ب_کارت #دریافت '
                                 '#موفق</span></html>"}}]},"transferInfo":{"$type":"MapValue","items":[{'
                                 '"key":"regarding","value":{"$type":"StringVal","text":"شماره انتقال: ۱۰۰۰۲\\nواریز '
                                 'کننده: *محمدس*\\nنام دریافت کننده: *آقاکریمی*\\nشهر محل دریافت: *جنت آباد*\\nمبلغ: '
                                 '*۱۰۰* ریال معادل *۰* افغانی"}},{"key":"isExpenditure","value":{"$type":"BooleanValue",'
                                 '"value":false}},{"key":"payer","value":{"$type":"Int64Val","value":"1497526823"}},'
                                 '{"key":"responseCode","value":{"$type":"StringVal","text":"00"}},{"key":"description",'
                                 '"value":{"$type":"StringVal","text":"رسید سه"}},{"key":"serviceName",'
                                 '"value":{"$type":"StringVal","text":"BAMDAD"}},{"key":"msgPeerId",'
                                 '"value":{"$type":"Int64Val","value":"1424339448"}},{"key":"msgUID",'
                                 '"value":{"$type":"StringVal","text":"713165279472439179-1547885000441"}},'
                                 '{"key":"receiver","value":{"$type":"Int64Val","value":"1424339448"}},{"key":"msgRid",'
                                 '"value":{"$type":"Int64Val","value":"713165279472439179"}},{"key":"amount",'
                                 '"value":{"$type":"Int64Val","value":"100"}},{"key":"date","value":{"$type":"Int64Val",'
                                 '"value":"1547885026141"}},{"key":"msgDate","value":{"$type":"Int64Val",'
                                 '"value":"1547885000441"}},{"key":"status","value":{"$type":"StringVal",'
                                 '"text":"SUCCESS"}},{"key":"requestId","value":{"$type":"StringVal",'
                                 '"text":"a3e79293-788b-4682-a25b-6db64aea7f38"}},{"key":"traceNo",'
                                 '"value":{"$type":"Int64Val","value":"113929"}},{"key":"receiptType",'
                                 '"value":{"$type":"StringVal","text":"MoneyTransfer"}},{"key":"msgPeerType",'
                                 '"value":{"$type":"Int64Val","value":"1"}}]}}}},"users":[[11,{"id":11,'
                                 '"accessHash":"3192746565014995892","name":"رسید تراکنش","sex":1,"about":null,'
                                 '"avatar":{"smallImage":{"fileLocation":{"fileId":"-7466032735434964736",'
                                 '"accessHash":"538643987","fileStorageVersion":1},"width":100,"height":100,'
                                 '"fileSize":1867},"largeImage":{"fileLocation":{"fileId":"9120643460453957889",'
                                 '"accessHash":"538643987","fileStorageVersion":1},"width":200,"height":200,'
                                 '"fileSize":3697},"fullImage":{"fileLocation":{"fileId":"2919809924124377345",'
                                 '"accessHash":"538643987","fileStorageVersion":1},"width":800,"height":800,'
                                 '"fileSize":15839}},"username":"receipt","isBot":true,"contactRecords":[],'
                                 '"timeZone":null,"preferredLanguages":[],"botCommands":[]}]],"groups":[]}')

    test_update_2 = FatSeqUpdate('{"$type":"FatSeqUpdate","seq":1342,"body":{"$type":"Message","peer":{"$type":"User",'
                                 '"id":1497526823,"accessHash":"42289642128192331"},"sender":{"$type":"User",'
                                 '"id":1497526823,"accessHash":"42289642128192331"},"date":"1547882922154",'
                                 '"randomId":"-4756969014585788658","message":{"$type":"BankMessage","message":{'
                                 '"$type":"ReceiptMessage","message":{"$type":"MapValue","items":[{"key":"fa",'
                                 '"value":{"$type":"StringVal","text":"<html><span><b>انتقال '
                                 'پول</b></span><br/><span>کارت ب کارت با موفقیت انجام شد.<br/>مبلغ: </span><span>۱۰۰ '
                                 'ریال</span><br/><span>کارت مبدا: </span><span>۶۰۳۷۹۹XXXXXX۷۰۷۲</span><br/><span>کارت '
                                 'مقصد: </span><span>۶۰۳۷۹۹XXXXXX۲۱۰۶</span><br/><span>صاحب کارت مقصد: </span><span>محمد '
                                 'اژدری</span><br/><span>بابت: </span><span>شماره انتقال: 614381\\nواریز کننده: '
                                 '*محمدس*\\nنام دریافت کننده: *محمدر*\\nشهر محل دریافت: *سداد*\\nمبلغ: *۱۰۰* ریال معادل '
                                 '*۰* افغانی</span><br/><span>توضیحات: </span><span>رسید دوم</span><br/><span>شماره '
                                 'پیگیری: </span><span>۹۰۲۷۸۸</span><br/><span>تاریخ انتقال: '
                                 '</span><span><date>۱۵۴۷۸۸۲۹۲۲۰۹۴</date></span><br/><span>#کارت_ب_کارت #انتقال '
                                 '#موفق</span></html>"}},{"key":"en","value":{"$type":"StringVal",'
                                 '"text":"<html><span><b>انتقال پول</b></span><br/><span>کارت ب کارت با موفقیت انجام '
                                 'شد.<br/>مبلغ: </span><span>۱۰۰ ریال</span><br/><span>کارت مبدا: '
                                 '</span><span>۶۰۳۷۹۹XXXXXX۷۰۷۲</span><br/><span>کارت مقصد: '
                                 '</span><span>۶۰۳۷۹۹XXXXXX۲۱۰۶</span><br/><span>صاحب کارت مقصد: </span><span>محمد '
                                 'اژدری</span><br/><span>بابت: </span><span>شماره انتقال: 614381\\nواریز کننده: '
                                 '*محمدس*\\nنام دریافت کننده: *محمدر*\\nشهر محل دریافت: *سداد*\\nمبلغ: *۱۰۰* ریال معادل '
                                 '*۰* افغانی</span><br/><span>توضیحات: </span><span>رسید دوم</span><br/><span>شماره '
                                 'پیگیری: </span><span>۹۰۲۷۸۸</span><br/><span>تاریخ انتقال: '
                                 '</span><span><date>۱۵۴۷۸۸۲۹۲۲۰۹۴</date></span><br/><span>#کارت_ب_کارت #انتقال '
                                 '#موفق</span></html>"}}]},"transferInfo":{"$type":"MapValue","items":[{'
                                 '"key":"regarding","value":{"$type":"StringVal","text":"شماره انتقال: 614381\\nواریز '
                                 'کننده: *محمدس*\\nنام دریافت کننده: *محمدر*\\nشهر محل دریافت: *سداد*\\nمبلغ: *۱۰۰* ریال '
                                 'معادل *۰* افغانی"}},{"key":"isExpenditure","value":{"$type":"BooleanValue",'
                                 '"value":false}},{"key":"payer","value":{"$type":"Int64Val","value":"1497526823"}},'
                                 '{"key":"responseCode","value":{"$type":"StringVal","text":"00"}},{"key":"description",'
                                 '"value":{"$type":"StringVal","text":"رسید دوم"}},{"key":"serviceName",'
                                 '"value":{"$type":"StringVal","text":"BAMDAD"}},{"key":"msgPeerId",'
                                 '"value":{"$type":"Int64Val","value":"1424339448"}},{"key":"msgUID",'
                                 '"value":{"$type":"StringVal","text":"723409154399732071-1547882833882"}},'
                                 '{"key":"receiver","value":{"$type":"Int64Val","value":"1424339448"}},{"key":"msgRid",'
                                 '"value":{"$type":"Int64Val","value":"723409154399732071"}},{"key":"amount",'
                                 '"value":{"$type":"Int64Val","value":"100"}},{"key":"date","value":{"$type":"Int64Val",'
                                 '"value":"1547882922094"}},{"key":"msgDate","value":{"$type":"Int64Val",'
                                 '"value":"1547882833882"}},{"key":"status","value":{"$type":"StringVal",'
                                 '"text":"SUCCESS"}},{"key":"requestId","value":{"$type":"StringVal",'
                                 '"text":"36e0e431-951e-4ec7-b7bf-ffe178c81979"}},{"key":"traceNo",'
                                 '"value":{"$type":"Int64Val","value":"902788"}},{"key":"receiptType",'
                                 '"value":{"$type":"StringVal","text":"MoneyTransfer"}},{"key":"msgPeerType",'
                                 '"value":{"$type":"Int64Val","value":"1"}}]}}}},"users":[[1497526823,{"id":1497526823,'
                                 '"accessHash":"42289642128192331","name":"S.shad","sex":1,"about":"سلام",'
                                 '"avatar":{"smallImage":{"fileLocation":{"fileId":"-381332758481862397",'
                                 '"accessHash":"1497526823","fileStorageVersion":1},"width":100,"height":100,'
                                 '"fileSize":4587},"largeImage":{"fileLocation":{"fileId":"-6251778147657514752",'
                                 '"accessHash":"1497526823","fileStorageVersion":1},"width":200,"height":200,'
                                 '"fileSize":14759},"fullImage":{"fileLocation":{"fileId":"-5031855972771626750",'
                                 '"accessHash":"1497526823","fileStorageVersion":1},"width":316,"height":316,'
                                 '"fileSize":70328}},"username":"sshad","isBot":false,"contactRecords":[],'
                                 '"timeZone":"Asia/Tehran","preferredLanguages":["fa-IR","fa"],"botCommands":[]}]],'
                                 '"groups":[]}')


class BotMessages:
    money_request_photo_message = PhotoMessage(name="image.png", file_id="8052119474392862211", access_hash="201707397",
                                               file_size=210162, mime_type="image/png", thumb=BotTexts.thumb,
                                               file_storage_version=1, caption_text=TextMessage(""),
                                               height=424, width=728)


class BotButtons:
    back_to_main_menu = TemplateMessageButton("بازگشت به منوی اصلی ")
    help = TemplateMessageButton("راهنمایی")
    register = TemplateMessageButton("ثبت نام")
    remittance = TemplateMessageButton("انتقال پول")
    money_changer = TemplateMessageButton("برادران جعفری")
    cities = [TemplateMessageButton("کابل"),
              TemplateMessageButton("هرات"),
              TemplateMessageButton("مزار شریف")]
    money_changer_branches = [TemplateMessageButton("کابل"),
                              TemplateMessageButton("هرات"),
                              TemplateMessageButton("مزار شریف")]


class ButtonText:
    cancel = "لغو"
    start = "شروع"
    back = "بازگشت به منو اصلی"
    help = "راهنما"
    # ========================
    register = "ثبت نام"
    remittance = "انتقال پول"
    money_changer = "افضلی-سخاوتی"
    provinces = ["کابل", "هرات", "مزار شریف", "قندهار"]


provinces_to_branch_dict = {"کابل": BotTexts.money_changer_kabol, "هرات": BotTexts.money_changer_harat,
                            "مزار شریف": BotTexts.money_changer_mazar}


class Step:
    request_sender_name = "request_sender_name"
    get_payment_amount_with_valid_input = "get_payment_amount_with_valid_input"
    send_report = "send_report"
    get_payment_amount = "get_payment_amount"
    help = "help"
    get_city_name = "get_city_name"
    get_receiver_name = "get_receiver_name"
    start_bot_for_logged_in_users = "start_bot_for_logged_in_users"
    start_resistance_conversation = "start_resistance_conversation"
    register = "register"
    start_bot_for_users_that_do_not_logged_in = "start_bot_for_users_that_do_not_logged_in"


class LogMessage:
    payment_is_done = "Payment with message_id {} is done."
    new_payment_added = "New payment added."
    user_added = "User with user_id {} joined to bot and added."
    db_error = "We have a db error in {} function."
    failed_step_message_sending = "failure {} message sending."
    successful_step_message_sending = "successful {} message sending."


class UserData:
    update = "update"
    logger = "logger"
    attempt = "attempt"
    message = "message"
    succedent_message = "succedent_message"
    user_id = "user_id"
    bot = "bot"
    step_name = "step_name"
    user_peer = "user_peer"
    kwargs = "kwargs"
