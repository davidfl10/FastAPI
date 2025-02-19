from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    street = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    floors = Column(Integer)
    rooms = Column(Integer)
    price = Column(Float)
    sold = Column(Boolean, default=False)
    sold_at = Column(Date, nullable=True)