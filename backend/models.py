from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.sql import func
from backend.database import Base

class Component(Base):
    __tablename__ = "components"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)


class ComponentPrice(Base):
    __tablename__ = "component_prices"

    id = Column(Integer, primary_key=True, index=True)
    component_id = Column(Integer, ForeignKey("components.id"))
    price = Column(Float, nullable=False)
    effective_from = Column(Date, nullable=False)


class Configuration(Base):
    __tablename__ = "configurations"

    id = Column(Integer, primary_key=True, index=True)

    frame_id = Column(Integer)
    gear_id = Column(Integer)
    tyre_id = Column(Integer)
    brake_id = Column(Integer)
    seat_id = Column(Integer)

    total_price = Column(Float)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now())