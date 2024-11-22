from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.payment import Payment
from ..schemas.payment import PaymentCreate, PaymentUpdate

def create(db: Session, request: PaymentCreate):
    new_payment = Payment(**request.dict())
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

def read_all(db: Session):
    return db.query(Payment).all()

def read_one(db: Session, payment_id: int):
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

def update(db: Session, request: PaymentUpdate, payment_id: int):
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    db_payment.payment_method = request.payment_method
    db_payment.amount_paid = request.amount_paid
    db_payment.payment_date = request.payment_date

    db.commit()
    db.refresh(db_payment)
    return db_payment

def delete(db: Session, payment_id: int):
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    db.delete(db_payment)
    db.commit()
    return {"detail": "Payment deleted successfully"}
