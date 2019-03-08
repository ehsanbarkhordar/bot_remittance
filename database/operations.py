from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from constant.templates import LogMessage
from configs import DatabaseConfig
from database.models import Base, MoneyChanger, MoneyChangerBranch
from balebot.utils.logger import Logger
from utils.utils import generate_random_number

logger = Logger.get_logger()

engine = create_engine(DatabaseConfig.database_url)
Session = sessionmaker(engine)
session = Session()


def create_all_table():
    Base.metadata.create_all(engine)
    return True


def delete_all_table():
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
        for obj in table_object:
            session.add(obj)
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

# def select_recent_charges(peer_id):
#     return session.query(RecentCharges).filter(RecentCharges.peer_id == peer_id).order_by(RecentCharges.date).all()

#
# def user_was_logged(user_id):
#     try:
#         user = session.query(Users).filter(Users.user_id == str(user_id)).one_or_none()
#         if user:
#             return True
#         else:
#             return False
#     except SQLAlchemyError as e:
#         logger.error(LogMessage.db_error.format(e, "user_was_logged"))
#         session.rollback()
#
#
# def get_owner_with_user_id(user_id):
#     try:
#         user = session.query(Users).filter(Users.user_id == user_id).one_or_none()
#         if user:
#             return user
#         else:
#             return False
#     except SQLAlchemyError as e:
#         logger.error(LogMessage.db_error.format(e, "get_owner_with_user_id"))
#         session.rollback()
#
#
# def add_payment_to_db(owner_user_id, receiver_name, city_name, amount, message_id):
#     tracking_code = generate_random_number_with_N_digits(4)
#     while tracking_code_is_repetitive(tracking_code):
#         tracking_code = generate_random_number_with_N_digits(4)
#
#     owner = get_owner_with_user_id(user_id=owner_user_id)
#     payment = Payments(receiver_name=receiver_name, destination_city_name=city_name, money_amount=amount,
#                        tracking_code=tracking_code, payment_is_done=False, owner=owner, message_id=message_id)
#     try:
#         session.add(payment)
#         session.commit()
#         logger.info(LogMessage.new_payment_added)
#     except SQLAlchemyError as e:
#         logger.error(LogMessage.db_error.format(e, "user_was_logged"))
#         session.rollback()
#
#
# def tracking_code_is_repetitive(tracking_code):
#     try:
#         all_payments = session.query(Payments).all()
#         if all_payments:
#             for payment in all_payments:
#                 if int(payment.tracking_code) == int(tracking_code):
#                     return True
#         return False
#     except SQLAlchemyError as e:
#         logger.error(LogMessage.db_error.format(e, "tracking_code_is_repetitive"))
#         session.rollback()
#
#
# def message_id_is_repetitive(message_id):
#     try:
#         all_payments = session.query(Payments).all()
#         if all_payments:
#             for payment in all_payments:
#                 if int(payment.message_id) == int(message_id):
#                     return True
#         return False
#     except SQLAlchemyError as e:
#         logger.error(LogMessage.db_error.format(e, "message_id_is_repetitive"))
#         session.rollback()
#
#
# def get_payment_with_message_id(message_id):
#     try:
#         payment = session.query(Payments).filter(Payments.message_id == str(message_id)).one_or_none()
#         if payment:
#             return payment
#         else:
#             return False
#     except SQLAlchemyError as e:
#         logger.error(LogMessage.db_error.format(e, "get_payment_with_message_id"))
#         session.rollback()
#
#
# def update_payment_is_done(message_id):
#     try:
#         payment = get_payment_with_message_id(message_id)
#         payment.payment_is_done = True
#         session.commit()
#         logger.info(LogMessage.payment_is_done.format(message_id))
#
#     except SQLAlchemyError as e:
#         logger.error(LogMessage.db_error.format(e, "update_payment_is_done"))
#         session.rollback()
#
#
# def get_all_payments_from_db():
#     try:
#         payments = session.query(Payments).all()
#         if payments:
#             return payments
#         else:
#             return False
#     except SQLAlchemyError as e:
#         logger.error(LogMessage.db_error.format(e, "get_all_payments_from_db"))
#         session.rollback()

#
# def generate_message_id():
#     payments = get_all_payments_from_db()
#     if payments:
#         message_ids = [payment.message_id for payment in payments]
#         max_message_id = max(message_ids)
#         new_message_id = int(max_message_id) + 1
#     else:
#         new_message_id = 10000
#
#     return new_message_id
