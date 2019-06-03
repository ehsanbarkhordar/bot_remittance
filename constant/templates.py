from balebot.models.base_models import FatSeqUpdate
from balebot.models.messages import TemplateMessageButton, PhotoMessage, TextMessage


class BotTexts:
    son = " ولد "
    wage = "یک میلیون تومان می شود {} افغانی"
    choose_province = "*ولایت* مورد نظر خود را انتخاب کنید:"
    no_money_changer_found = "هیچ صرافی یافت نشد!"
    branch_deleted_successfully = "شعبه مورد نظر با موفقیت حذف شد."
    no_branches_found = "هیچ شعبه ای یافت نشد!"
    choose_branch_for_remove = "شعبه مورد نظر برای حذف را انتخاب کنید:"
    branch_inserted_successfully = "شعبه با موفقیت افزوده شد."
    dollar_afghani_updated_successfully = " نسبت افغانی به دلار با موفقیت تغییر یافت.\n" \
                                          "نسبت جدید: *{}*"
    enter_new_dollar_afghani = "نسبت جدید دلار به افغانی را وارد کنید:"
    undefined = "نامشخص"
    card_number_updated_successfully = "شماره کارت با موفقیت تغییر یافت.\n" \
                                       "شماره کارت جدید: *{}*"
    dollar_rial_updated_successfully = " نسبت دلار به ریال با موفقیت تغییر یافت.\n" \
                                       "نسبت جدید: *{}*"
    enter_new_dollar_rial = "نسبت جدید دلار به ریال را وارد کنید:"
    enter_new_card_number = "شماره کارت جدید را وارد کنید:"
    error = "*خطایی رخ داده است. *\nلطفا دوباره امتحان کنید."
    remittance_fee_percent_updated_successfully = " درصد انتقال پول با موفقیت تغییر یافت.\n" \
                                                  "درصد جدید: *{}* درصد"
    enter_new_remittance_fee_percent = "لطفا درصد انتقال پول را به عدد وارد کنید:"
    enter_branch_address = "آدرس شعبه را با دقت وارد کنید:"
    choose_or_enter_province = "ولایت را وارد یا از بین گزینه ها انتخاب کنید:"
    enter_sender_father_name = "لطفا نام پدر پرداخت کننده را وارد کنید:"
    enter_sender_name = "لطفا *نام و نام خانوادگی* واریز کننده را وارد کنید:"
    choose_one_money_changer = "لطفا صرافی موردنظر خود را از بین صرافی‌های زیر به دقت *انتخاب* کنید:"
    back_to_main_menu = "بازگشت به منوی اصلی"
    invalid_amount = "ورودی اشتباه است،\nلطفاً مبلغ را به *عدد* وارد کنید:"
    enter_amount = "لطفاً مبلغ را به *ریال* وارد کنید:"
    enter_city_name = "لطفاً نام *شهر محل دریافت پول* را *انتخاب* و یا *وارد* کنید: "
    enter_receiver_name = "لطفاً *نام* دریافت کننده پول را *وارد* کنید:"
    enter_receiver_father_name = "لطفاً *نام پدر* دریافت کننده پول را *وارد* کنید:"
    choose_one_option = "لطفاً یک گزینه را *انتخاب* کنید:"
    money_changer_info = "نام صرافی شما: *{}*\n" \
                         "شماره کارت ست شده: {}\n" \
                         "نسبت دلار به ریال: *{}*\n" \
                         "نسبت افغانی به دلار: *{}*\n" \
                         "درصد انتقال پول: *{}*\n\n"

    enter_your_name = "لطفاً نام و نام خانوادگی خود را وارد کنید:"
    welcome_message = "سلام خوش آمدید،‌ لطفاً یکی از گزینه های زیر را *انتخاب* کنید:"
    help_message = "به کمک این بازو می توانید پیام انتقال" \
                   " مبلغ دلخواه خودتان را برای فرد مورد نظرتان در *افغانستان* ارسال کنید.\n" \
                   "1. لازم است ابتدا ثبت نام کنید و سپس از طریق گزینه ارسال پیام انتقال پول و انتخاب صرافی مسئول تحویل مبلغ، نرخ تبدیل ارز را ببینید.\n" \
                   "2. در ادامه نام دریافت کننده پول از صرافی انتخاب شده در افغانستان را وارد کنید.\n" \
                   "3. در مرحله بعد، شهر محل دریافت پول را مشخص کنید.\n" \
                   "4. در نهایت، مبلغ مورد نظرتان به ريال را که به حساب فرد مورد اعتماد صراف می رود، وارد کنید تا پیام پرداخت پول را مشاهده کنید. با زدن کلید پرداخت، مبلغ مورد نظر شما(در وجه ریال) به حساب فرد مورد اعتماد صراف می رود.\n" \
                   "5. پس از پرداخت پول، رسید انتقال وجه و شماره ای که باید با آن پول را از صراف یا نماینده وی در افغانستان، به افغانی دریافت کنید، در اختیار شما قرار می گیرد. اگر بخواهید این پیام برای بستگان شما نیز فرستاده می شود تا با ارائه آن به صرافی مراجعه و مبلغ را از صراف یا نماینده وی بگیرند."

    report_message = "*رسید انتقال*\n\n" \
                     "انتقال پول با *موفقیت* انجام شد.\n" \
                     "تاریخ انتقال: *{}*\n" \
                     "⬅️ واریز کننده:  {}\n" \
                     "➡️ دریافت کننده:  {}\n" \
                     "کد انتقال:  *{}*\n" \
                     "ولایت:  {}\n" \
                     "🏦 آدرس:  {}\n" \
                     "🇮🇷 مبلغ ریال پرداخت شده:  *{}*\n" \
                     "🇦🇫 مبلغ افغانی قابل دریافت:  *{}*"

    hyper_link = "[{}](send: {})"
    select = "انتخاب"

    money_changer_branch = "{address}\n" \
                           "[انتخاب](send: {branch_id})"
    fence = "\n+++++++++++++++++++++++++++++++++++++++\n"

    thumb = "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAA4KCw0LCQ4NDA0QDw4RFiQXFhQUFiwgIRokNC43NjMuMjI6QVNGOj1OPjIySGJJTlZYXV5dOEVmbWVabFNbXVn/2wBDAQ8QEBYTFioXFypZOzI7WVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVn/wAARCAA0AFoDASIAAhEBAxEB/8QAGwABAQADAQEBAAAAAAAAAAAAAAUBBAYDBwL/xAA1EAACAgEDAgMGAwcFAAAAAAABAgMRAAQFIRIxIkFRBhNhcYGRFULwFCMyUqGx0UOSk9Lh/8QAGQEBAAMBAQAAAAAAAAAAAAAAAAECBAMF/8QAJhEAAgECBAUFAAAAAAAAAAAAAAECAxEEITFBEiIykfAUQlFhgf/aAAwDAQACEQMRAD8A+kYxjAGZzGZwBmpucEmp0MkUUjxuaIdGKsKIPFefwPB8+M95ZRELYGvXyHz9MkbhuOpSfTRRS6eFZpH07m+plkKhkHV2UkX3Dd14N8Abei1s0jJFqYlEhXl4zaEgC+DyLPVQ54HJs1m6ro5cKysUPSwBvpNXR+hH3z597S6fWR6yVZZNUdOaQNJ0lZPzdRCqI7Jvir8NnuMo7Hv8c7R6hkWTWamYI508QctEGKqHKnwkdQayACAQBkXzsc41FKTj8HZYxjJOgxjGAMYzOAeGrRGgLSSmFYyJC/V0ha55+HrecxuvtNqNs1U+lkjEg6Or3gkVGQEd1BB7Uf4hyb8qvpNbE0kEqkK6MvSY3W1Yc2CPOxxWQm9ntTrpk/b9Yz6aIdKofEXAJIuxfUDVNZNWO9s0MrNSa5dSvtuvG46eSaOmjVx7tlPLqVVgSPI81z6X2IyVuu1zar3gjjno14YyFdKPUCrdXStEWK5LdHV4VOWNujnh99HO1r13EoUAInSBVjvyGP1zcySxxmp9mHbRO25zJKFkV0DyNKwJ4Kq0hpbJA+JAJ8lWtsOk05jZmjdpoSEJkYEiqKqwBolRRHHHVfcsTcZQ6lWAKkUQfPNDbNBNotRrmkmSSPUSiVAqFSvhC0TZvhV9PP5AV4Ve5QxjGCwzOYzOAYyX7QQCbb3ZUImQWsqDxxgkdRQ/zV2+NZTa+k9JAauCRYyPpX3GTdpizXp0NBGAUAXQoi74s/7RfehDP1sGl1un0wbXyNJJIi0GN+7A/IfUi+/nlfGMBKysMZh3WNGd2CqossTQA9c5LcN2m3SR4tOzR6DlSappvX4gfr4DnUqRpx4pFZzUcty3rN70mlkMSltRKDTJCL6e/c9h27XeTH3/AFrspSHTwqR2cmQ39KyUGighBsJGP19883kkmUrHD4T+aQ9I+HHf+2eZPGVJdOSOTk932LH43uHrpf8Aib/tntDv2pUgTwxSAnkxkpQ+Ruz9RnOqupSZI5JyEI8JVAbPpZ8893gdhxqJARyDS8H7ZT1NWLzl52IUnsmdfo910usYIrGOU/6cnDH5eR4HkTWb2cBA0skdsUYrwVIohh6n/wAygu4a9VCrrJKAoWqH+pFn65qjjksprP6Okaja0OtJoHJPs3uM257c0+oCB/eFfAKFUP8AOMZ6B03K+MYwSc37XTP06LSX+6nclwLs9NUPlz/QZNAAAAFAdgMYzyMe+dIz++X4T9MPeGDUvzJIzA+gFHt9v75QxjMlXVeblaOhM3TUvHIIlC1QYEjkG88fxaf+SP7H/OMZohFOCujPOTU3Zmxt2peeeYsALAJAur7fr5ZRxjM9XqNFHpP/2Q=="

    money_request_caption = "کد انتقال: *{}*\n" \
                            "نام واریز کننده: *{}*\n" \
                            "نام دریافت کننده: *{} فرزند {}*\n" \
                            "ولایت محل دریافت: *{}*\n" \
                            "آدرس صرافی: {}\n" \
                            "مبلغ: *{}* ریال معادل *{}* افغانی"

    test_update_22 = FatSeqUpdate(
        '{"$type":"FatSeqUpdate","seq":1257,"body":{"$type":"Message","peer":{"$type":"User","id":11,"accessHash":"-350560019069227129"},"sender":{"$type":"User","id":11,"accessHash":"-350560019069227129"},"date":"1552625889354","randomId":"2274453424573922247","message":{"$type":"BankMessage","message":{"$type":"ReceiptMessage","message":{"$type":"MapValue","items":[{"key":"fa","value":{"$type":"StringVal","text":"<html><span><b>انتقال پول</b></span><br/><span>مبلغ دریافتی: </span><span><font color=\'#40d0a3\'>۲۰+ ریال</font></span><br/><span>کارت مبدا: </span><span>۶۰۳۷۹۹XXXXXX۱۰۴۰</span><br/><span>کارت مقصد: </span><span>۶۰۳۷۶۹XXXXXX۵۴۴۸</span><br/><span>صاحب کارت مقصد: </span><span>محمد ایوبی </span><br/><span>واریزکننده: </span><span>احسان برخوردار - @ehsan</span><br/><span>بابت: </span><span>کد انتقال: *B۱۰۰۱*\\nنام واریز کننده: *حسن*\\nنام دریافت کننده: *مصطفی فرزند خالد*\\nولایت محل دریافت: *کابل*\\nآدرس صرافی: سینمای پامیر، جاده میوند، حیدری مارکیت، منزل اول، اتاق ۱۳۷، صرافی ضیاءالحق\\nمبلغ: *۲۰* ریال معادل *۰* افغانی</span><br/><span>توضیحات: </span><span>توضیحات</span><br/><span>شماره پیگیری: </span><span>۹۹۵۱۹۶</span><br/><span>تاریخ انتقال: </span><span><date>۱۵۵۲۶۲۵۸۸۹۲۹۳</date></span><br/><span>#کارت_ب_کارت #دریافت #موفق</span><br/><br/><span>🛎 خبر خوش داریم:</span><br/><span>🎊 در بله، جشنوارهٔ «پولتو راحت بریز» برپاست!</span><br/><span>🎉 تراکنش بزن و جایزه ببر! 👇 </span><br/><span><a href=\'http://bit.ly/2XAvW0L\'>http://bit.ly/2XAvW0L</a></span></html>"}},{"key":"en","value":{"$type":"StringVal","text":"<html><span><b>انتقال پول</b></span><br/><span>مبلغ دریافتی: </span><span><font color=\'#40d0a3\'>۲۰+ ریال</font></span><br/><span>کارت مبدا: </span><span>۶۰۳۷۹۹XXXXXX۱۰۴۰</span><br/><span>کارت مقصد: </span><span>۶۰۳۷۶۹XXXXXX۵۴۴۸</span><br/><span>صاحب کارت مقصد: </span><span>محمد ایوبی </span><br/><span>واریزکننده: </span><span>احسان برخوردار - @ehsan</span><br/><span>بابت: </span><span>کد انتقال: *B۱۰۰۱*\\nنام واریز کننده: *حسن*\\nنام دریافت کننده: *مصطفی فرزند خالد*\\nولایت محل دریافت: *کابل*\\nآدرس صرافی: سینمای پامیر، جاده میوند، حیدری مارکیت، منزل اول، اتاق ۱۳۷، صرافی ضیاءالحق\\nمبلغ: *۲۰* ریال معادل *۰* افغانی</span><br/><span>توضیحات: </span><span>توضیحات</span><br/><span>شماره پیگیری: </span><span>۹۹۵۱۹۶</span><br/><span>تاریخ انتقال: </span><span><date>۱۵۵۲۶۲۵۸۸۹۲۹۳</date></span><br/><span>#کارت_ب_کارت #دریافت #موفق</span><br/><br/><span>🛎 خبر خوش داریم:</span><br/><span>🎊 در بله، جشنوارهٔ «پولتو راحت بریز» برپاست!</span><br/><span>🎉 تراکنش بزن و جایزه ببر! 👇 </span><br/><span><a href=\'http://bit.ly/2XAvW0L\'>http://bit.ly/2XAvW0L</a></span></html>"}}]},"transferInfo":{"$type":"MapValue","items":[{"key":"regarding","value":{"$type":"StringVal","text":"کد انتقال: *B۱۰۰۱*\\nنام واریز کننده: *حسن*\\nنام دریافت کننده: *مصطفی فرزند خالد*\\nولایت محل دریافت: *کابل*\\nآدرس صرافی: سینمای پامیر، جاده میوند، حیدری مارکیت، منزل اول، اتاق ۱۳۷، صرافی ضیاءالحق\\nمبلغ: *۲۰* ریال معادل *۰* افغانی"}},{"key":"isExpenditure","value":{"$type":"BooleanValue","value":false}},{"key":"payer","value":{"$type":"Int64Val","value":"201707397"}},{"key":"responseCode","value":{"$type":"StringVal","text":"00"}},{"key":"description","value":{"$type":"StringVal","text":"توضیحات"}},{"key":"serviceName","value":{"$type":"StringVal","text":"BAMDAD"}},{"key":"msgPeerId","value":{"$type":"Int64Val","value":"373225249"}},{"key":"msgUID","value":{"$type":"StringVal","text":"1089955259788824658-1552622923355"}},{"key":"receiver","value":{"$type":"Int64Val","value":"373225249"}},{"key":"msgRid","value":{"$type":"Int64Val","value":"1089955259788824658"}},{"key":"amount","value":{"$type":"Int64Val","value":"20"}},{"key":"date","value":{"$type":"Int64Val","value":"1552625889293"}},{"key":"msgDate","value":{"$type":"Int64Val","value":"1552622923355"}},{"key":"status","value":{"$type":"StringVal","text":"SUCCESS"}},{"key":"requestId","value":{"$type":"StringVal","text":"1e95227c-6b54-4708-9a2c-d61ae16ed84a"}},{"key":"traceNo","value":{"$type":"Int64Val","value":"995196"}},{"key":"receiptType","value":{"$type":"StringVal","text":"MoneyTransfer"}},{"key":"msgPeerType","value":{"$type":"Int64Val","value":"1"}}]}}}},"users":[[11,{"id":11,"accessHash":"-350560019069227129","name":"رسید تراکنش","sex":1,"about":null,"avatar":{"smallImage":{"fileLocation":{"fileId":"-7466032735434964736","accessHash":"538643987","fileStorageVersion":1},"width":100,"height":100,"fileSize":1867},"largeImage":{"fileLocation":{"fileId":"9120643460453957889","accessHash":"538643987","fileStorageVersion":1},"width":200,"height":200,"fileSize":3697},"fullImage":{"fileLocation":{"fileId":"2919809924124377345","accessHash":"538643987","fileStorageVersion":1},"width":800,"height":800,"fileSize":15839}},"username":"receipt","isBot":true,"contactRecords":[],"timeZone":null,"preferredLanguages":[],"botCommands":[]}]],"groups":[]}')


class BotMessages:
    money_request_photo_message = PhotoMessage(name="image.png", file_id="8052119474392862211", access_hash="201707397",
                                               file_size=210162, mime_type="image/png", thumb=BotTexts.thumb,
                                               file_storage_version=1, caption_text=TextMessage(""),
                                               height=424, width=728)


class BotButtons:
    remove_branch = TemplateMessageButton("حذف یک شعبه")
    update_dollar_afghani = TemplateMessageButton("تغییر نسبت افغانی به دلار")
    update_card_number = TemplateMessageButton("تغییر شماره کارت")
    update_dollar_rial = TemplateMessageButton("تغییر نسبت دلار به ریال")
    update_remittance_fee_percent = TemplateMessageButton("تغییر درصد حق الزحمه انتقال پول")
    register_branch = TemplateMessageButton("ثبت شعبه جدید")
    back_to_main_menu = TemplateMessageButton("بازگشت به منوی اصلی")
    help = TemplateMessageButton("راهنمایی")
    register = TemplateMessageButton("ثبت نام")
    remittance = TemplateMessageButton("انتقال پول")
    money_changer_panel = TemplateMessageButton("منو صرافی")
    user_panel = TemplateMessageButton("منو کاربر")

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


class Patterns:
    passive_loan_val = 'passive-{}'
    active_loan_val = 'active-{}'
    passive_loan = '^passive-([0-9]+|[۰-۹]+)$'
    active_loan = '^active-([0-9]+|[۰-۹]+)$'
    number_only = '^([0-9]+|[۰-۹]+)$'
    eight_digits_number = "^[0-9]{8}$|^[۰-۹]{8}$"
    numbers = '([0-9]+|[۰-۹]+)'
    any_match = "(.*)"
    float_numbers = "^[0-9]*(?:\.[0-9]*)?$"


class Step:
    payment_success = "payment_success"
    request_receiver_father_name = "request_receiver_father_name"
    request_sender_father_name = "request_sender_father_name"
    user_panel = "user_panel"
    request_money_changer = "request_money_changer"
    request_province = "request_province"
    request_branch = "request_branch"
    request_receiver_name = "request_receiver_name"
    request_amount = "request_amount"
    send_payment_message = "send_payment_message"
    insert_branch = "insert_branch"
    request_remittance_fee_percent = "request_remittance_fee_percent"
    request_dollar_afghani = "request_dollar_afghani"
    request_dollar_rial = "request_dollar_rial"
    update_money_changer = "update_money_changer"
    request_card_number = "request_card_number"
    update_remittance_fee_percent = "update_remittance_fee_percent"
    request_branch_address = "request_branch_address"
    request_province_name = "request_province_name"
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
    payment_is_done = "Payment with code {} is done."
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
