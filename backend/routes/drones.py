from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import DroneMission, Product
from typing import List

router = APIRouter()

@router.get("/drones/missions")
def get_active_drone_missions(db: Session = Depends(get_db)):
    missions = db.query(DroneMission).filter(DroneMission.status == "in-transit").all()
    output = []

    for m in missions:
        product = db.query(Product).filter(Product.id == m.product_id).first()
        output.append({
            "id": m.id,
            "drone_id": m.drone_id,
            "product_name": product.name if product else "Unknown",
            "destination": m.destination,
            "status": m.status,
            "eta": m.eta
        })

    return output
