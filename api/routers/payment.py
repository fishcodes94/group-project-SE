from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import payment as controller
from ..schemas import payment as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Payments'],
    prefix="/payments"
)

@router.post("/", response_model=schema.PaymentResponse)
def create(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.PaymentResponse])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{payment_id}", response_model=schema.PaymentResponse)
def read_one(payment_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, payment_id=payment_id)

@router.put("/{payment_id}", response_model=schema.PaymentResponse)
def update(payment_id: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, payment_id=payment_id)

@router.delete("/{payment_id}")
def delete(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, payment_id=payment_id)
