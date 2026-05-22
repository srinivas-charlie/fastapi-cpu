from db import engine, Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablenmae__ = "users"

    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)