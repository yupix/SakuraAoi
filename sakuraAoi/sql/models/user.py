from sqlalchemy import Column, Integer, String
from db import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(500))
    username = Column(String(500), unique=True)
    love = Column(Integer)
