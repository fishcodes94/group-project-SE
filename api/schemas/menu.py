from typing import List, Optional
from pydantic import BaseModel
from .menu_item import MenuItem



class MenuBase(BaseModel):
    menu_name: str
    description: Optional[str] = None
    category: str

class MenuCreate(MenuBase):
    pass

class MenuUpdate(BaseModel):
    menu_name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None

class Menu(MenuBase):
    id: int
    menu_items: List[MenuItem] = []  # Include menu items

    class Config:
        from_attributes  = True

# Response Model for API
class MenuResponse(MenuBase):
    id: int
    menu_items: List[MenuItem] = []  # Include menu items

    class Config:
        orm_mode = True  # Ensure that Pydantic can serialize ORM models