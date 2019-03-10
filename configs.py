import os


class BotConfig:
    re_uploading_max_try = int(os.environ.get('RE_UPLOADING_MAX_TRY', 3))
    resending_max_try = int(os.environ.get('RESENDING_MAX_TRY', 3))
    admin_list = os.environ.get('ADMIN_LIST', "201707397")
    bot_token = os.environ.get('BOT_TOKEN', "c37abc81e3d95f0c0198ce8df87ebe15686bca50")  # @tap_bot
    # 1146359648: a9f06fec310400da3d0e3c6f3bbd8e9bba34089a
    # bot_token = os.environ.get('BOT_TOKEN', "e8e48df04ff639e34025270b5ee8c1c888aae390")  # @remittancebot
    log_level = int(os.environ.get('LOG_LEVEL', 20))


class DatabaseConfig:
    db_string_main = 'postgresql://{}:{}@{}:{}/{}'
    database_url = db_string_main.format(os.environ.get('POSTGRES_USER', "ehsan"),
                                         os.environ.get('POSTGRES_PASSWORD', "ehsan1379"),
                                         os.environ.get('POSTGRES_HOST', "localhost"),
                                         os.environ.get('POSTGRES_PORT', "5432"),
                                         os.environ.get('POSTGRES_DB', "bot_remittance"))
