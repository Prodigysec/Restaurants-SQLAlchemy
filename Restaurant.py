from .database import Base
from sqlalchemy import Column, Integer, String


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True, index=True)
    name = Column(String(), nullable=False)
    price = Column(Integer(), nullable=False)
