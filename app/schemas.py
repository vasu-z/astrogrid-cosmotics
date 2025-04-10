from pydantic import BaseModel
from datetime import date
from typing import Optional

class CargoCreate(BaseModel):
    name: str
    weight: float
    priority: int
    expiry_date: Optional[date] = None

class Cargo(CargoCreate):
    id: int
    glow_color: str

    class Config:
        orm_mode = True


