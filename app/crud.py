from sqlalchemy.orm import Session
from app import models, schemas

def create_cargo(db: Session, cargo: schemas.CargoCreate):
    db_item = models.CargoItem(**cargo.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
def get_all_cargo(db: Session):
    return db.query(models.CargoItem).all()
