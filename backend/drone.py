from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import Product
from backend.schemas import ProductOut
from backend.utils.drone_controller import send_drone_to_user

router = APIRouter()

@router.post("/drone/dispatch/{product_id}", response_model=ProductOut)
def dispatch_drone(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    try:
        # Trigger drone dispatch (this can run async or task queue later)
        send_drone_to_user(location_description=product.preferred_location)
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Drone dispatch failed: {str(e)}")
