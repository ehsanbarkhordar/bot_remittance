from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database.connect import Base


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(String)
    access_hash = Column(String)
    payments = relationship("Payments", back_populates="owner")

    def __init__(self, name, user_id, access_hash):
        self.name = str(name)
        self.user_id = str(user_id)
        self.access_hash = access_hash


class Payments(Base):
    __tablename__ = "Payments"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('Users.id'))
    owner = relationship("Users", back_populates="payments")
    receiver_name = Column(String)
    destination_city_name = Column(String)
    money_amount = Column(String)
    payment_is_done = Column(Boolean)
    tracking_code = Column(String)
    message_id = Column(String)

    def __init__(self, receiver_name, destination_city_name, money_amount, payment_is_done, tracking_code, owner, message_id):
        self.destination_city_name = destination_city_name
        self.receiver_name = receiver_name
        self.money_amount = money_amount
        self.payment_is_done = payment_is_done
        self.tracking_code = tracking_code
        self.owner = owner
        self.message_id = str(message_id)


class MoneyChanger(Base):
    __tablename__ = "MoneyChanger"
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    access_hash = Column(String)
    name = Column(String)
    account_number = Column(String)

    def __init__(self, name, user_id, access_hash, acount_numer):
        self.name = name
        self.user_id = str(user_id)
        self.access_hash = str(access_hash)
        self.account_number = str(acount_numer)


"""
   question_id = Column(Integer, ForeignKey('Questions.id'))

destination_city = Column(String)
    money_amount = Column(String)
    payment_done = Column(Boolean)
    tracking_code = Column(String)
    
"""
