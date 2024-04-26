from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship

class DbClient(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

    movement = relationship('DbMovement', back_populates='client')

class DbBranch(Base):
    __tablename__ = 'branch'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)

    movement = relationship('DbMovement', back_populates='branch')

class DbItem(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    kind = Column(String)
    size = Column(String)
    gender = Column(String)
    available = Column(Boolean)

    movement = relationship('DbMovement', back_populates='item')

class DbPrice(Base):
    __tablename__ = 'price'
    id = Column(Integer, primary_key=True, index=True)
    days = Column(String)
    price = Column(Float)

class DbMovement(Base):
    __tablename__ = 'movement'
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('item.id'))
    branch_id = Column(Integer, ForeignKey('branch.id'))
    client_id = Column(Integer, ForeignKey('client.id'))
    starts = Column(DateTime)
    ends = Column(DateTime)
    price = Column(Float)

    item = relationship('DbItem', back_populates='movement')
    branch = relationship('DbBranch', back_populates='movement')
    client = relationship('DbClient', back_populates='movement')