from sqlalchemy import Column, Integer, Float, ForeignKey, String, Boolean, DateTime
from datetime import datetime
from app.db.base import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    old_price = Column(Float, nullable=False)
    new_price = Column(Float, nullable=False)

    alert_type = Column(String, nullable=False)  # "price_drop"
    is_read = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)