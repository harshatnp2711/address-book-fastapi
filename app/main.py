from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas, crud
from .utils import calculate_distance

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/addresses", response_model=schemas.AddressOut)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)

@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    return crud.delete_address(db, address_id)

@app.get("/addresses/nearby")
def nearby(latitude: float, longitude: float, distance_km: float, db: Session = Depends(get_db)):
    addresses = db.query(models.Address).all()
    return [
        a for a in addresses
        if calculate_distance(latitude, longitude, a.latitude, a.longitude) <= distance_km
    ]

