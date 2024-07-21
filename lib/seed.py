# lib/seed.py

from sqlalchemy.orm import sessionmaker
from models import Base, engine, Game, Review
from faker import Faker
import random

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add a console message so we can see output when the seed file runs
print("Seeding games...")

# Clear existing data
session.query(Game).delete()
session.query(Review).delete()
session.commit()

fake = Faker()

# Generate games
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for _ in range(10)
]

session.bulk_save_objects(games)
session.commit()

# Generate reviews for each game
for game in games:
    reviews = [
        Review(
            score=random.randint(1, 10),
            comment=fake.sentence(),
            game_id=game.id
        )
        for _ in range(5)
    ]
    session.bulk_save_objects(reviews)

session.commit()

print("Seeding complete.")
