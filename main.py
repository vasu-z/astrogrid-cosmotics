from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API route to create a new cargo item
@app.post("/cargo/")
def create_cargo(cargo: schemas.CargoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_cargo(db=db, cargo=cargo)
    except Exception as e:
        print(" ERROR:", e)
        return {"error": str(e)}

@app.get("/cargo/")
def read_cargo(db: Session = Depends(get_db)):
    return crud.get_all_cargo(db)
