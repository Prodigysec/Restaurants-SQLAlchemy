from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'),nullable=False)
    Customer_id = Column(Integer(), ForeignKey('customers.id'), nullable=False) 
    star_rating = Column(Integer(), nullable=False)
    customer = relationship("Customer", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews")

    @property
    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'restaurant_id={self.restaurant_id}, ' + \
            f'Customer_id={self.Customer_id}, ' + \
            f'star_rating={self.star_rating})'
    
    @property
    def full_review(self):
        return f'Review for {self.restaurant.name} by {self.customer.full_name}: {self.star_rating} stars.'
