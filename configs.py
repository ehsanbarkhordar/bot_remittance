import os


class BotConfig:
    re_uploading_max_try = int(os.environ.get('RE_UPLOADING_MAX_TRY', 3))
    resending_max_try = int(os.environ.get('RESENDING_MAX_TRY', 3))
    admin_list = os.environ.get('ADMIN_LIST', "201707397")
    bot_token = os.environ.get('BOT_TOKEN', "2938aa8c0d1c81909eb7316af1c5b21c144715d7")  # @my_test_bot
    # bot_token = os.environ.get('BOT_TOKEN', "e8e48df04ff639e34025270b5ee8c1c888aae390")  # @remittancebot
    log_level = int(os.environ.get('LOG_LEVEL', 20))
    money_changer_account_number = os.environ.get('MONEY_CHANGER_ACCOUNT_NUMBER', "6037997503351810")


class DatabaseConfig:
    db_string_main = 'postgresql://{}:{}@{}:{}/{}'
    database_url = db_string_main.format(os.environ.get('POSTGRES_USER', "ehsan"),
                                         os.environ.get('POSTGRES_PASSWORD', "ehsan1379"),
                                         os.environ.get('POSTGRES_HOST', "localhost"),
                                         os.environ.get('POSTGRES_PORT', "5432"),
                                         os.environ.get('POSTGRES_DB', "bot_remittance"))
