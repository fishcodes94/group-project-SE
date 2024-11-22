from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menu_name = Column(String(100), unique=True, nullable=False)  # Name of the menu, e.g., "Lunch Menu"
    description = Column(String(300), nullable=True)  # Optional description of the menu
    category = Column(String(100), nullable=False)  # Category of the menu, e.g., "Starters", "Main Course"

    menu_items = relationship("MenuItem", back_populates="menu")
