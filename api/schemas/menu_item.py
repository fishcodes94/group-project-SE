
"""
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich




class MenuItemBase(BaseModel):
    sandwich_id: int
    menu_id: int

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    sandwich_id: Optional[int] = None
    menu_id: Optional[int] = None

class MenuItem(MenuItemBase):
    id: int
    sandwich: Sandwich = None  # Include sandwich information

    class Config:
        from_attributes  = True
###

"""

# In your api/schemas/menu_item.py
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

class MenuItemBase(BaseModel):
    sandwich_id: int
    menu_id: int

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    sandwich_id: Optional[int] = None
    menu_id: Optional[int] = None

class MenuItem(MenuItemBase):
    id: int
    sandwich: Sandwich  # Include sandwich information

    class Config:
        from_attributes = True

class MenuItemResponse(MenuItemBase):
    id: int
    sandwich: Sandwich  # Include sandwich information

    class Config:
        from_attributes = True
