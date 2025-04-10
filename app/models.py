from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class CargoItem(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    weight = Column(Float, nullable=False)
    priority = Column(Integer, nullable=False)
    expiry_date = Column(Date, nullable=True)
    glow_color = Column(String, default="none")
