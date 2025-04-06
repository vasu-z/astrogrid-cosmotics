from pydantic import BaseModel
from datetime import date

class CargoCreate(BaseModel):
    name: str
    weight: float
    priority: str
    expiry_date: date


