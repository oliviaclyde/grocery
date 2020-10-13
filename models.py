from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    qty = Column(Integer)
    price = Column(Float)
    purchased = Column(Boolean) 

