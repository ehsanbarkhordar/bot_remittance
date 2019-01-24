import os


class BotConfig:
    re_uploading_max_try = int(os.environ.get('RE_UPLOADING_MAX_TRY', 3))
    resending_max_try = int(os.environ.get('RESENDING_MAX_TRY', 3))
    # bot_token = os.environ.get('BOT_TOKEN', "9f2965cd2350a5a79fd404135639abe7d4f59543")  # @my_test_bot
    bot_token = os.environ.get('BOT_TOKEN', "e8e48df04ff639e34025270b5ee8c1c888aae390")  # @remittancebot
    log_level = int(os.environ.get('LOG_LEVEL', 20))
    money_changer_account_number = os.environ.get('MONEY_CHANGER_ACCOUNT_NUMBER', "6037997479512106")


class DbConfig:
    db_user = os.environ.get('POSTGRES_USER', "muhammad")
    db_password = os.environ.get('POSTGRES_PASSWORD', "1540487768")
    db_host = os.environ.get('POSTGRES_HOST', "localhost")
    db_name = os.environ.get('POSTGRES_DB', "resistance_bot_db")
    db_port = os.environ.get('POSTGRES_PORT', "5432")
    database_url = "postgresql://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name)
