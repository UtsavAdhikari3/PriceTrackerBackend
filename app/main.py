from fastapi import FastAPI
from app.db.base import Base
from app.db.database import engine

from app.models import user, product, price_history, watchlist, alert
from app.api.router import api_router

app = FastAPI()

app.include_router(api_router)