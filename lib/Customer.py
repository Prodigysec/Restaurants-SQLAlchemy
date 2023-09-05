from .database import Base, SessionLocal
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
    
    @property
    def favorite_restaurant(self):
        favourite = None
        highest_rating = 0

        for review in self.reviews:
            if review.star_rating > highest_rating:
                highest_rating = review.star_rating
                favourite = review.restaurant

        return favourite
    
    @property
    def add_review(self,restaurant,rating):
        review = Review(restaurant_review=restaurant,customer_id=self.id,star_rating=rating)
        SessionLocal.add(review)
        SessionLocal.commit()

    @property
    def delete_reviews(self):
        pending_delete = SessionLocal.query(Review).filter(Review.customer_id == self.id)
        pending_delete.delete()
        SessionLocal.commit()
        