from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.menu import Menu
from ..schemas.menu import MenuCreate, MenuUpdate


def create(db: Session, request: MenuCreate):
    db_menu = db.query(Menu).filter(Menu.menu_name == request.menu_name).first()
    if db_menu:
        raise HTTPException(status_code=400, detail="Menu already exists")

    new_menu = Menu(**request.dict())
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu


def read_all(db: Session):
    return db.query(Menu).all()


def read_one(db: Session, menu_id: int):
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    if not db_menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    return db_menu


def update(db: Session, request: MenuUpdate, menu_id: int):
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    if not db_menu:
        raise HTTPException(status_code=404, detail="Menu not found")

    db_menu.menu_name = request.menu_name
    db_menu.description = request.description
    db_menu.category = request.category

    db.commit()
    db.refresh(db_menu)
    return db_menu


def delete(db: Session, menu_id: int):
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    if not db_menu:
        raise HTTPException(status_code=404, detail="Menu not found")

    db.delete(db_menu)
    db.commit()
    return {"detail": "Menu deleted successfully"}
