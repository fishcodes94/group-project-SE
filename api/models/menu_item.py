from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menu_id = Column(Integer, ForeignKey("menus.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))

    menu = relationship("Menu", back_populates="menu_items")
    sandwich = relationship("Sandwich", back_populates="menu_items")
