# backend/routes/order_notification.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/order-status")
def order_status():
    return {"status": "order is being processed"}
