# backend/routes/qr_code.py

from fastapi import APIRouter, HTTPException
from backend.utils.qr_generator import generate_product_qr

router = APIRouter()

@router.get("/product-qr", summary="Generate QR code for product")
def get_qr_code(product_id: int):
    """
    Returns base64 image of a QR code linking to the product page.
    """
    if not product_id:
        raise HTTPException(status_code=400, detail="Product ID is required")

    product_url = f"https://smartbiz.com/products/{product_id}"
    qr_base64 = generate_product_qr(product_url)
    
    return {
        "product_id": product_id,
        "qr_code_base64": qr_base64,
        "link": product_url
    }
