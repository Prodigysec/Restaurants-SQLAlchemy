from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True, index=True)
    name = Column(String(), nullable=False)
    price = Column(Integer(), nullable=False)

    reviews = relationship('Review', back_populates='restaurant')
