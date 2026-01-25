from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, datetime

from app.database import SessionLocal, engine
from app import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AstroGrid Backend MVP")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def compute_urgency(priority, expiry_date, weight):
    score = priority * 20
    if expiry_date:
        days = (expiry_date - date.today()).days
        score += max(0, 30 - days)
    if weight < 1:
        score += 10
    return min(100, score)

def compute_retrieval_cost(blockers):
    time_sec = 10 + len(blockers) * 12
    risk = round(min(1.0, 0.05 * len(blockers)), 2)
    return time_sec, risk

@app.post("/cargo/", response_model=schemas.Cargo)
def create_cargo(cargo: schemas.CargoCreate, db: Session = Depends(get_db)):
    return crud.create_cargo(db=db, cargo=cargo)

@app.get("/cargo/", response_model=list[schemas.Cargo])
def read_cargo(db: Session = Depends(get_db)):
    return crud.get_all_cargo(db)

@app.get("/cargo/sorted", response_model=list[schemas.Cargo])
def read_sorted_cargo(db: Session = Depends(get_db)):
    return crud.get_sorted_cargo(db)

@app.get("/optimize")
def optimize(db: Session = Depends(get_db)):
    base = crud.optimize_cargo(db)
    return {
        "status": "optimized",
        "decision": "High priority and near-expiry items placed for fastest access",
        "confidence": 0.87,
        "items": base.get("items", [])
    }

@app.get("/retrieve/{cargo_id}")
def retrieve(cargo_id: int, db: Session = Depends(get_db)):
    result = crud.retrieve_cargo(db, cargo_id)
    blockers = result.get("blockers_removed", [])
    time_sec, risk = compute_retrieval_cost(blockers)
    return {
        "retrieved": result.get("retrieved"),
        "blockers_removed": blockers,
        "estimated_time_sec": time_sec,
        "risk_score": risk
    }

@app.get("/export")
def export(db: Session = Depends(get_db)):
    return crud.export_layout(db)

@app.get("/logs")
def logs():
    return crud.read_logs()

@app.get("/visual/{cargo_id}")
def visualize_one(cargo_id: int, db: Session = Depends(get_db)):
    item = crud.visualize_cargo(db, cargo_id)
    urgency = compute_urgency(item["priority"], item["expiry_date"], item["weight"])
    item["urgency_score"] = urgency
    return item

@app.get("/visual")
def visualize_all(db: Session = Depends(get_db)):
    items = crud.get_all_cargo(db)
    out = []
    for i in items:
        v = crud.visualize_cargo(db, i.id)
        v["urgency_score"] = compute_urgency(v["priority"], v["expiry_date"], v["weight"])
        out.append(v)
    return out

@app.get("/seed")
def seed(db: Session = Depends(get_db)):
    demo = [
        {"name":"Emergency Oxygen","weight":6.5,"priority":5,"expiry_date":"2026-01-28"},
        {"name":"Med Kit","weight":1.2,"priority":4,"expiry_date":"2026-03-01"},
        {"name":"Food Pack","weight":2.5,"priority":3,"expiry_date":"2026-02-05"},
        {"name":"Spare Bolt","weight":0.2,"priority":1,"expiry_date":None}
    ]
    created = []
    for d in demo:
        try:
            created.append(crud.create_cargo(db, schemas.CargoCreate(**d)).name)
        except:
            pass
    return {"created": created}

@app.get("/health")
def health(db: Session = Depends(get_db)):
    items = crud.get_all_cargo(db)
    critical = 0
    for i in items:
        urgency = compute_urgency(i.priority, i.expiry_date, i.weight)
        if urgency > 80:
            critical += 1
    status = "EMERGENCY" if critical > 2 else "NOMINAL"
    return {
        "status": status,
        "critical_items": critical,
        "timestamp": datetime.utcnow().isoformat()
    }
