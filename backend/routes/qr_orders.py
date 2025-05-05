from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models import Product
from backend.utils.qr_utils import generate_qr_code

router = APIRouter()

@router.post("/products/{product_id}/generate-qr", summary="🔲 Generate QR for a product")
def create_product_qr(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    qr_url = f"https://yourdomain.com/order/{product_id}"
    qr_path = generate_qr_code(qr_url, filename=f"product_{product_id}")

    # (Optional) Save to DB
    product.qr_code_url = qr_path
    db.commit()

    return {"qr_code_path": qr_path, "link": qr_url}

@router.get("/generate-qr", summary="🔳 Generate QR Code for Product Order")
def get_qr(data: str = Query(..., description="Product link or ID")):
    return generate_qr_code(data)