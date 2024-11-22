from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.resources import Resource
from ..schemas.resources import ResourceCreate, ResourceUpdate

def create(db: Session, request: ResourceCreate):
    new_resource = Resource(**request.dict())
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource

def read_all(db: Session):
    return db.query(Resource).all()

def read_one(db: Session, resource_id: int):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if not db_resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return db_resource

def update(db: Session, request: ResourceUpdate, resource_id: int):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if not db_resource:
        raise HTTPException(status_code=404, detail="Resource not found")

    db_resource.item = request.item
    db_resource.amount = request.amount

    db.commit()
    db.refresh(db_resource)
    return db_resource

def delete(db: Session, resource_id: int):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if not db_resource:
        raise HTTPException(status_code=404, detail="Resource not found")

    db.delete(db_resource)
    db.commit()
    return {"detail": "Resource deleted successfully"}
