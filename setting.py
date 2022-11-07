import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session

engine = sqlalchemy.create_engine("sqlite:///sample_db.sqlite3", echo=True)

Base = declarative_base()


class Customer(Base):

    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    age = Column(Integer)

    __tablename__ = "customer"


session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
