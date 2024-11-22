from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.menu_item import MenuItem
from ..schemas.menu_item import MenuItemCreate, MenuItemUpdate

def create(db: Session, request: MenuItemCreate):
    new_menu_item = MenuItem(**request.dict())
    db.add(new_menu_item)
    db.commit()
    db.refresh(new_menu_item)
    return new_menu_item

def read_all(db: Session):
    return db.query(MenuItem).all()

def read_one(db: Session, menu_item_id: int):
    db_menu_item = db.query(MenuItem).filter(MenuItem.id == menu_item_id).first()
    if not db_menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return db_menu_item

def update(db: Session, request: MenuItemUpdate, menu_item_id: int):
    db_menu_item = db.query(MenuItem).filter(MenuItem.id == menu_item_id).first()
    if not db_menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    db_menu_item.menu_id = request.menu_id
    db_menu_item.sandwich_id = request.sandwich_id

    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

def delete(db: Session, menu_item_id: int):
    db_menu_item = db.query(MenuItem).filter(MenuItem.id == menu_item_id).first()
    if not db_menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    db.delete(db_menu_item)
    db.commit()
    return {"detail": "Menu item deleted successfully"}
