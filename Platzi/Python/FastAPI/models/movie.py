from sqlalchemy import Column, Integer, String, Float

from config.database import Base


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    overview = Column(String)
    year = Column(String)
    rating = Column(Float)
    category = Column(String)
