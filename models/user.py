from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user_autogenerate"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)