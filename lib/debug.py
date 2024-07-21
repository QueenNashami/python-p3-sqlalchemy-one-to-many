# lib/debug.py

from sqlalchemy.orm import sessionmaker
from models import Base, engine, Game, Review

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Access the first review
review = session.query(Review).first()
print(review)
print(review.game)

# Access the first game
game = session.query(Game).first()
print(game)
print(game.reviews)
