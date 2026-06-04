from sqlalchemy.orm import Session
from backend.models import Component
from backend.models import ComponentPrice
from backend.models import Configuration

def create_component(db: Session, name: str, category: str):
    component = Component(
        name=name,
        category=category
    )

    db.add(component)
    db.commit()
    db.refresh(component)

    return component

def create_price(
    db: Session,
    component_id: int,
    price: float,
    effective_from
):
    component_price = ComponentPrice(
        component_id=component_id,
        price=price,
        effective_from=effective_from
    )

    db.add(component_price)
    db.commit()
    db.refresh(component_price)

    return component_price

from sqlalchemy import desc
from backend.models import ComponentPrice

def get_latest_price(db, component_id):
    return (
        db.query(ComponentPrice)
        .filter(ComponentPrice.component_id == component_id)
        .order_by(desc(ComponentPrice.effective_from))
        .first()
    )

def save_configuration(
        db,
        frame_id,
        gear_id,
        tyre_id,
        brake_id,
        seat_id,
        total_price
):

    config = Configuration(
        frame_id=frame_id,
        gear_id=gear_id,
        tyre_id=tyre_id,
        brake_id=brake_id,
        seat_id=seat_id,
        total_price=total_price
    )

    db.add(config)
    db.commit()
    db.refresh(config)

    return config
def get_all_configurations(db):
    return db.query(Configuration).all()
def get_components(db):
    components = db.query(Component).all()

    return [
        {
            "id": component.id,
            "name": component.name,
            "category": component.category
        }
        for component in components
    ]   
    
def get_price_for_date(
    db,
    component_id,
    pricing_date
):
    return (
        db.query(ComponentPrice)
        .filter(
            ComponentPrice.component_id == component_id,
            ComponentPrice.effective_from <= pricing_date
        )
        .order_by(
            ComponentPrice.effective_from.desc()
        )
        .first()
    )
def get_price_for_date(
    db,
    component_id,
    pricing_date
):
    return (
        db.query(ComponentPrice)
        .filter(
            ComponentPrice.component_id == component_id,
            ComponentPrice.effective_from <= pricing_date
        )
        .order_by(
            ComponentPrice.effective_from.desc()
        )
        .first()
    )