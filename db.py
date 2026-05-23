from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:root@db:5432/postgres"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bine=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



