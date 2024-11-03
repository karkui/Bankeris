from sqlalchemy import Column, Integer, String, create_engine, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///bankeris.sqlite")
Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    surname = Column("surname", String)
    social_nr = Column("social_nr", Integer)
    phone_nr = Column("phone_nr", String)
    accounts = relationship("Account", back_populates="person")


class Account(Base):
    __tablename__ = "account"
    id = Column("id", Integer, primary_key=True)
    iban_nr = Column("iban_nr", String)
    balance = Column("balance", Float)
    person_id = Column("person_id", Integer, ForeignKey("person.id"))
    person = relationship("Person", back_populates="accounts")
    bank_id = Column("bank_id", Integer, ForeignKey("bank.id"))
    bank = relationship("Bank", back_populates="accounts")

class Bank(Base):
    __tablename__ = "bank"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    adress = Column("adress", String)
    swif_code = Column("swif_code", String)
    accounts = relationship("Account", back_populates="bank")

Base.metadata.create_all(engine)


