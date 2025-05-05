# backend/routes/smart_orders.py

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime

from backend.db import get_db
from backend.models import Order, Product, User
from backend.auth import get_current_user

router = APIRouter()

class SmartOrderRequest(BaseModel):
    product_id: int
    quantity: int

@router.post("/place", summary="Place order via QR/NFC")
def place_smart_order(
    order: SmartOrderRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == order.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.stock < order.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    total_price = order.quantity * product.price

    new_order = Order(
        user_id=current_user.id,
        product_id=product.id,
        quantity=order.quantity,
        total=total_price,
        status="pending",
        created_at=datetime.utcnow()
    )

    product.stock -= order.quantity  # real-time stock update

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return {
        "message": "✅ Order placed successfully via QR/NFC",
        "order_id": new_order.id,
        "product": product.name,
        "quantity": order.quantity,
        "total": total_price
    }
