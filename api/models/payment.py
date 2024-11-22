from datetime import datetime

from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    payment_method = Column(String(50), nullable=False)  # E.g., Credit Card, PayPal
    amount_paid = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))

    order = relationship("Order", back_populates="payment")
