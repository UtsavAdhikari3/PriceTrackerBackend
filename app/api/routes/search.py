from fastapi import APIRouter, Query
from app.services.search_service import search_products

router = APIRouter()


@router.get("/search")
def search(q: str = Query(..., description="Search query")):
    results = search_products(q)
    return results