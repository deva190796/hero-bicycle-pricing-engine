from pydantic import BaseModel
from datetime import date

class ComponentCreate(BaseModel):
    name: str
    category: str

class ComponentResponse(ComponentCreate):
    id: int

    class Config:
        from_attributes = True
class ComponentPriceCreate(BaseModel):
    component_id: int
    price: float
    effective_from: date

class PriceCalculationRequest(BaseModel):
    frame_id: int
    gear_id: int
    tyre_id: int
    brake_id: int
    seat_id: int