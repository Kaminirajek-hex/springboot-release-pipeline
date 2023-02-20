from sqlalchemy import Boolean, Column, Float, Integer, String
from db.base import Base


class Sample(Base):
    __tablename__ = "Sample"
    id = Column(Integer, primary_key=True)
    
    name = Column(String(50), nullable=False)
    number = Column(, nullable=False)