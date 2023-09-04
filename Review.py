from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'),nullable=False)
    Customer_id = Column(Integer(), ForeignKey('customers.id'), nullable=False) 
    star_rating = Column(Integer(), nullable=False)
