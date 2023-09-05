from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.associationproxy import association_proxy
from .Review import Review


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    first_names = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)

    reviews = relationship('Review', back_populates='customer')
    restaurant = association_proxy("reviews", 'restaurant_review', creator=lambda v: Review(restaurant_review=v))

    def __repr__(self):
        return f'Customer(id={self.id}, ' + \
            f'first_names={self.first_names}, ' + \
            f'last_name={self.last_name})'