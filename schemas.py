from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class PropertyBase(BaseModel):
    type: str = Field(..., pattern="^(house|building)$")
    street: str
    city: str
    state: str
    floors: int
    rooms: int
    price: float
    sold: Optional[bool] = False
    sold_at: Optional[date] = None

class PropertyCreate(PropertyBase):
    pass

class PropertyUpdate(BaseModel):
    price: Optional[float] = None
    sold: Optional[bool] = None
    sold_at: Optional[date] = None

class PropertyResponse(PropertyBase):
    id: int

    class Config:
        from_attributes = True
