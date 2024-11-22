
"""
from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    payment_method: str
    amount_paid: float

class PaymentCreate(PaymentBase):
    order_id: int

class PaymentUpdate(BaseModel):
    payment_method: Optional[str] = None
    amount_paid: Optional[float] = None

class Payment(PaymentBase):
    id: int
    payment_date: str

    class Config:
        from_attributes  = True


"""

# In your api/schemas/payment.py
from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    payment_method: str
    amount_paid: float

class PaymentCreate(PaymentBase):
    order_id: int

class PaymentUpdate(BaseModel):
    payment_method: Optional[str] = None
    amount_paid: Optional[float] = None

class Payment(PaymentBase):
    id: int
    payment_date: str

    class Config:
        from_attributes = True

# Define the PaymentResponse schema
class PaymentResponse(PaymentBase):
    id: int
    payment_date: str

    class Config:
        from_attributes = True
