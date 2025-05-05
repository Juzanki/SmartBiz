from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.models import Product
from backend.db import get_db
from backend.utils.inventory_ai import check_refill_needed

router = APIRouter()

@router.get("/check-stock-alerts", summary="🚨 Smart Inventory Refill Suggestions")
def smart_inventory_check(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    suggestions = []

    for product in products:
        suggestion = check_refill_needed(product)
        if suggestion:
            suggestions.append(suggestion)

    return {"recommendations": suggestions}


@router.get("/inventory/suggestions", summary="Suggest restocking for fast-selling products")
def suggest_inventory_refill(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user.business_name:
        raise HTTPException(status_code=400, detail="Business not linked to user profile")

    suggestions = check_stock_levels(db, current_user.id)
    return {"suggestions": suggestions}
