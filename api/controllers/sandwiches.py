from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.sandwiches import Sandwich
from ..schemas.sandwiches import SandwichCreate, SandwichUpdate

def create(db: Session, request: SandwichCreate):
    new_sandwich = Sandwich(**request.dict())
    db.add(new_sandwich)
    db.commit()
    db.refresh(new_sandwich)
    return new_sandwich

def read_all(db: Session):
    return db.query(Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if not db_sandwich:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return db_sandwich

def update(db: Session, request: SandwichUpdate, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if not db_sandwich:
        raise HTTPException(status_code=404, detail="Sandwich not found")

    db_sandwich.sandwich_name = request.sandwich_name
    db_sandwich.price = request.price

    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def delete(db: Session, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if not db_sandwich:
        raise HTTPException(status_code=404, detail="Sandwich not found")

    db.delete(db_sandwich)
    db.commit()
    return {"detail": "Sandwich deleted successfully"}
