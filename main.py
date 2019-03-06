from bot.remittance_bot import updater
from database.operations import create_all_table

if __name__ == '__main__':
    create_all_table()
    updater.run()
