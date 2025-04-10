from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime
import logging

logging.basicConfig(filename='cargo.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def get_glow_color(expiry_date):
    if not expiry_date:
        return "none"
    today = datetime.now().date()
    if expiry_date < today:
        return "red"  
    elif (expiry_date - today).days <= 5:
        return "yellow" 
    else:
        return "blue"  

def create_cargo(db: Session, cargo: schemas.CargoCreate):
    db_item = models.CargoItem(**cargo.dict())
    db_item.glow_color = get_glow_color(db_item.expiry_date)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    
    logging.info(f"Created cargo: {db_item.name}, Priority: {db_item.priority}, Glow: {db_item.glow_color}")
    return db_item

def get_all_cargo(db: Session):
    cargo_list = db.query(models.CargoItem).all()
    for item in cargo_list:
        item.glow_color = get_glow_color(item.expiry_date)
    return cargo_list

def get_sorted_cargo_by_weight_priority(db: Session):
    cargo_list = db.query(models.CargoItem).all()
    cargo_list.sort(key=lambda x: (-x.priority, x.weight))  
    for item in cargo_list:
        item.glow_color = get_glow_color(item.expiry_date)
    return cargo_list

