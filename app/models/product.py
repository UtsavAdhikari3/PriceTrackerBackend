from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)
    image_url = Column(String, nullable=True)

    current_price = Column(Float, nullable=False)
    initial_price = Column(Float, nullable=False)

    last_checked_at = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)