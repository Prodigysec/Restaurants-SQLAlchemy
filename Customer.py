from .database import Base
from sqlalchemy import Column, Integer, String


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)