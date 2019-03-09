from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from configs import DatabaseConfig
from database.models import Base, MoneyChanger, MoneyChangerBranch
from balebot.utils.logger import Logger

logger = Logger.get_logger()

engine = create_engine(DatabaseConfig.database_url)
Session = sessionmaker(engine)
session = Session()


def create_all_table():
    Base.metadata.create_all(engine)
    return True


def drop_all_table():
    Base.metadata.drop_all(engine)
    return True


def db_persist(func):
    def persist(*args, **kwargs):
        func(*args, **kwargs)
        try:
            session.commit()
            logger.info("success calling db func: " + func.__name__)
            return True
        except SQLAlchemyError as e:
            logger.error(e.args)
            session.rollback()
            return False

    return persist


@db_persist
def insert_to_table(table_object):
    if isinstance(table_object, list):
        session.add_all(table_object)
    else:
        session.add(table_object)


@db_persist
def delete_from_table(table_object):
    if isinstance(table_object, list):
        for obj in table_object:
            session.delete(obj)
    else:
        session.delete(table_object)


@db_persist
def insert_or_update(table_object):
    return session.merge(table_object)


@db_persist
def update_money_changer_remittance_fee_percent(money_changer, percent):
    if isinstance(money_changer, MoneyChanger):
        money_changer.remittance_fee_percent = percent


@db_persist
def update_money_changer_dollar_rial(money_changer, dollar_rial):
    if isinstance(money_changer, MoneyChanger):
        money_changer.dollar_rial = dollar_rial


@db_persist
def update_money_changer_dollar_afghani(money_changer, dollar_afghani):
    if isinstance(money_changer, MoneyChanger):
        money_changer.dollar_afghani = dollar_afghani


@db_persist
def update_money_changer_card_number(money_changer, card_number):
    if isinstance(money_changer, MoneyChanger):
        money_changer.card_number = card_number


def select_money_changer_by_peer_id(peer_id):
    return session.query(MoneyChanger).filter(MoneyChanger.peer_id == peer_id).one_or_none()


def select_money_changer_by_id(money_changer_id):
    return session.query(MoneyChanger).filter(MoneyChanger.id == money_changer_id).one_or_none()


def select_money_changers():
    return session.query(MoneyChanger).all()


def select_all_province_names():
    return [r.province_name for r in session.query(MoneyChangerBranch.province).distinct().all()]


def select_branches_by_money_changer_id(money_changer_id):
    return session.query(MoneyChangerBranch).filter(MoneyChangerBranch.money_changer_id == money_changer_id).all()
