from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import menu as controller
from ..schemas import menu as schema
from ..dependencies.database import get_db



router = APIRouter(
    tags=['Menus'],
    prefix="/menus"
)

@router.post("/", response_model=schema.MenuResponse)
def create(request: schema.MenuCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.MenuResponse])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{menu_id}", response_model=schema.MenuResponse)
def read_one(menu_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, menu_id=menu_id)

@router.put("/{menu_id}", response_model=schema.MenuResponse)
def update(menu_id: int, request: schema.MenuUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, menu_id=menu_id)

@router.delete("/{menu_id}")
def delete(menu_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, menu_id=menu_id)
