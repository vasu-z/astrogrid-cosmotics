import time
import os
import psycopg2
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
for i in range(10):
    try:
        conn = psycopg2.connect(DB_URL)
        conn.close()
        break
    except psycopg2.OperationalError:
        time.sleep(2)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cosmotics Cargo API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/cargo/", response_model=schemas.Cargo)
def create_cargo(cargo: schemas.CargoCreate, db: Session = Depends(get_db)):
    return crud.create_cargo(db=db, cargo=cargo)

@app.get("/cargo/", response_model=list[schemas.Cargo])
def read_cargo(db: Session = Depends(get_db)):
    return crud.get_all_cargo(db)

@app.get("/cargo/sorted", response_model=list[schemas.Cargo])
def read_sorted_cargo(db: Session = Depends(get_db)):
    return crud.get_sorted_cargo_by_weight_priority(db)
