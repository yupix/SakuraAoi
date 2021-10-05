import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///aoi_db.sqlite3', echo=True)
Base = declarative_base()
session = sessionmaker(bind=engine)()


def init():
    Base.metadata.create_all(bind=engine)
