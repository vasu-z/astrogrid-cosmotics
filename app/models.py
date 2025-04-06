from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class CargoItem(Base):
    __tablename__ = "cargo_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    weight = Column(Float)  
    priority = Column(String)  
    expiry_date = Column(Date)  

