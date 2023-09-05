from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True, index=True)
    name = Column(String(), nullable=False)
    price = Column(Integer(), nullable=False)

    reviews = relationship('Review', back_populates='restaurant')

    @property
    def __repr__(self):
        return f'Restaurant(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'price={self.price})'

    @classmethod
    def fanciest_restaurant(session):
        fanciest_restaurant = session.query(Restaurant).order_by(Restaurant.price.desc()).first()
        return fanciest_restaurant
    
    
    @property
    def all_reviews(self):
        return [f'Review for {self.name} by {review.customer.full_name}: {review.star_rating} stars.' for review in self.reviews]

