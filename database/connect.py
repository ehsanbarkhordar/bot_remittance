from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from configs import DbConfig

engine = create_engine(DbConfig.database_url, echo=True)

_SessionFactory = sessionmaker(bind=engine)
session = Session(engine)
Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()