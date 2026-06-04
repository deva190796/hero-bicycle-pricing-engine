from fastapi import FastAPI
from backend.database import engine, Base
from backend import models
from sqlalchemy.orm import Session
from fastapi import Depends
from backend.database import get_db
from backend.schemas import ComponentCreate
from backend.crud import create_component
from backend.schemas import ComponentPriceCreate
from backend.crud import create_price
from backend.schemas import PriceCalculationRequest
from backend.pricing_service import calculate_bicycle_price
from backend.crud import get_components

app = FastAPI(
    title="Hero Bicycle Pricing Engine"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Hero Bicycle Pricing Engine Running"
    }
@app.post("/components")
def add_component(
    component: ComponentCreate,
    db: Session = Depends(get_db)
):
    return create_component(
        db,
        component.name,
        component.category
    )
    
@app.post("/prices")
def add_price(
    price: ComponentPriceCreate,
    db: Session = Depends(get_db)
):
    return create_price(
        db,
        price.component_id,
        price.price,
        price.effective_from
    )
@app.post("/calculate-price")
def calculate_price(
    request: PriceCalculationRequest,
    db: Session = Depends(get_db)
):
    return calculate_bicycle_price(db, request)

from backend.crud import (
    save_configuration,
    get_all_configurations
)
@app.post("/save-configuration")
def save_bicycle(
    request: PriceCalculationRequest,
    db: Session = Depends(get_db)
):

    result = calculate_bicycle_price(
        db,
        request
    )

    return save_configuration(
        db,
        request.frame_id,
        request.gear_id,
        request.tyre_id,
        request.brake_id,
        request.seat_id,
        result["total_price"]
    )
@app.get("/configurations")
def get_configurations(
    db: Session = Depends(get_db)
):
    return get_all_configurations(db)

@app.get("/components")
def fetch_components(
    db: Session = Depends(get_db)
):
    return get_components(db)
@app.get("/test")
def test():
    return {"message": "working"}