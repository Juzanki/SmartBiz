from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import Order, Product, ReferralLog, User
from backend.dependencies import get_current_user
from datetime import datetime
from pydantic import BaseModel


router = APIRouter(prefix="/orders", tags=["Orders"])

class CheckoutRequest(BaseModel):
    product_id: int

@router.post("/checkout")
def create_order(
    payload: CheckoutRequest,
    request: Request,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == payload.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Create order (basic logic)
    order = Order(
        user_id=current_user.id,
        product_id=product.id,
        price=product.price,
        created_at=datetime.utcnow()
    )
    db.add(order)

    # Handle referral tracking
    ref_by = request.session.get("ref_by")
    if ref_by:
        ref_user = db.query(User).filter(User.username == ref_by).first()
        if ref_user and ref_user.id != current_user.id:
            commission = round(product.price * 0.10, 2)  # 10% referral fee
            referral = ReferralLog(
                promoter_id=ref_user.id,
                product_name=product.name,
                buyer_name=current_user.username,
                amount=commission,
                status="pending",
                created_at=datetime.utcnow()
            )
            db.add(referral)

    db.commit()
    return {"message": "Order created successfully"}
