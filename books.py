from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
import mydatabase

Base = declarative_base()
mydb = mydatabase.MyDB()


class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(30), nullable=False)
    author = Column(String, nullable=False)
    year_published = Column(Integer, nullable=False)
    type = Column(Integer(), nullable=False)