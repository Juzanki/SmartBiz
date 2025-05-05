from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import Product
from backend.auth import get_current_user
from backend.schemas import ProductOut
from typing import List

router = APIRouter()

@router.get("/products/search", response_model=List[ProductOut], summary="🔍 Auto Search Products")
def search_products(
    query: str = Query(..., min_length=2, description="Search keyword"),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    results = db.query(Product).filter(Product.name.ilike(f"%{query}%")).all()
    return results
