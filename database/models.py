import datetime

from sqlalchemy import Column, String, Integer, Text, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MoneyChanger(Base):
    __tablename__ = "MoneyChanger"
    id = Column(Integer, primary_key=True, autoincrement=True)
    peer_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    card_number = Column(String, nullable=False)
    dollar_rial = Column(Float, default=4200)
    dollar_afghani = Column(Float, default=100)
    remittance_fee_percent = Column(Float, default=1)

    def __init__(self, peer_id, name, card_number, dollar_rial, dollar_afghani, remittance_fee_percent):
        self.peer_id = peer_id
        self.name = name
        self.card_number = card_number
        self.dollar_rial = dollar_rial
        self.dollar_afghani = dollar_afghani
        self.remittance_fee_percent = remittance_fee_percent


class MoneyChangerBranch(Base):
    __tablename__ = "MoneyChangerBranch"
    id = Column(Integer, primary_key=True, autoincrement=True)
    money_changer_id = Column(Integer, nullable=False)
    province = Column(String, nullable=False)
    address = Column(Text, nullable=False)

    def __init__(self, money_changer_id, province, address):
        self.money_changer_id = money_changer_id
        self.address = address
        self.province = province


class PaymentRequest(Base):
    __tablename__ = "PaymentRequest"
    id = Column(Integer, primary_key=True)
    message_id = Column(String, nullable=False)
    payer_peer_id = Column(String, nullable=False)
    money_changer_peer_id = Column(String, nullable=False)

    sender_name = Column(String)
    receiver_name = Column(String)
    province = Column(String)
    money_changer_branch_id = Column(Integer)
    remittance_amount = Column(String)
    date_time = Column(DateTime)

    def __init__(self, message_id, payer_peer_id, money_changer_peer_id, sender_name, receiver_name, province,
                 money_changer_branch_id, remittance_amount, date_time=datetime.datetime.now()):
        self.message_id = message_id
        self.payer_peer_id = str(payer_peer_id)
        self.money_changer_peer_id = str(money_changer_peer_id)
        self.sender_name = sender_name
        self.receiver_name = receiver_name
        self.province = province
        self.money_changer_branch_id = money_changer_branch_id
        self.remittance_amount = remittance_amount
        self.date_time = date_time
