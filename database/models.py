from sqlalchemy import Column, String, Integer, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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

    def __init__(self, peer_id, name, account_number):
        self.peer_id = peer_id
        self.name = name
        self.card_number = account_number


class MoneyChangerBranch(Base):
    __tablename__ = "MoneyChangerBranch"
    id = Column(Integer, primary_key=True, autoincrement=True)
    money_changer_id = Column(Integer, nullable=False)
    province = Column(String, nullable=False)
    address = Column(Text, nullable=False)

    def __init__(self, money_changer_id, address, province):
        self.money_changer_id = money_changer_id
        self.address = address
        self.province = province

# class Payments(Base):
#     __tablename__ = "Payments"
#     id = Column(Integer, primary_key=True)
#     owner_id = Column(Integer, ForeignKey('Users.id'))
#     owner = relationship("Users", back_populates="payments")
#     receiver_name = Column(String)
#     destination_city_name = Column(String)
#     money_amount = Column(String)
#     payment_is_done = Column(Boolean)
#     tracking_code = Column(String)
#     message_id = Column(String)
#
#     def __init__(self, receiver_name, destination_city_name, money_amount, payment_is_done, tracking_code, owner,
#                  message_id):
#         self.destination_city_name = destination_city_name
#         self.receiver_name = receiver_name
#         self.money_amount = money_amount
#         self.payment_is_done = payment_is_done
#         self.tracking_code = tracking_code
#         self.owner = owner
#         self.message_id = str(message_id)
