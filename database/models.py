from sqlalchemy import Column, String, Integer, Text, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MoneyChanger(Base):
    __tablename__ = "money_changers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    peer_id = Column(Integer, nullable=False)
    access_hash = Column(String)
    name = Column(String, nullable=False)
    card_number = Column(String, nullable=False)
    dollar_rial = Column(Float, default=12500)
    dollar_afghani = Column(Float, default=75)
    remittance_fee_percent = Column(Float, default=1)

    def __init__(self, peer_id, name, card_number, dollar_rial, dollar_afghani, remittance_fee_percent,
                 access_hash=None):
        self.peer_id = peer_id
        if access_hash:
            self.access_hash = access_hash
        self.name = name
        self.card_number = card_number
        self.dollar_rial = dollar_rial
        self.dollar_afghani = dollar_afghani
        self.remittance_fee_percent = remittance_fee_percent


class MoneyChangerBranch(Base):
    __tablename__ = "money_changer_branches"
    id = Column(Integer, primary_key=True, autoincrement=True)
    money_changer_id = Column(Integer, nullable=False)
    province = Column(String, nullable=False)
    address = Column(Text, nullable=False)

    def __init__(self, money_changer_id, province, address):
        self.money_changer_id = money_changer_id
        self.address = address
        self.province = province


class PaymentRequest(Base):
    __tablename__ = "payment_requests"
    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)
    money_changer_peer_id = Column(Integer, nullable=False)
    money_changer_access_hash = Column(String, nullable=False)
    payer_peer_id = Column(Integer, nullable=False)
    payer_access_hash = Column(String, nullable=False)

    sender_name = Column(String)
    receiver_name = Column(String)
    province = Column(String)
    money_changer_branch_id = Column(Integer)
    branch_address = Column(Text)
    rial_amount = Column(Float)
    afghani_amount = Column(Float)
    creation_date_time = Column(DateTime)

    pay_date_time = Column(DateTime)
    is_done = Column(Boolean, default=False)

    def __init__(self, code, payer_peer_id, payer_access_hash, money_changer_peer_id, money_changer_access_hash,
                 sender_name, receiver_name, province, branch_address, rial_amount, afghani_amount,
                 money_changer_branch_id, creation_date_time):
        self.code = code
        self.money_changer_peer_id = money_changer_peer_id
        self.money_changer_access_hash = money_changer_access_hash
        self.payer_peer_id = payer_peer_id
        self.payer_access_hash = payer_access_hash

        self.sender_name = sender_name
        self.receiver_name = receiver_name
        self.province = province
        self.money_changer_branch_id = money_changer_branch_id
        self.branch_address = branch_address
        self.rial_amount = rial_amount
        self.afghani_amount = afghani_amount
        self.creation_date_time = creation_date_time
