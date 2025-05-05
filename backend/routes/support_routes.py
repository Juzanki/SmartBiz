from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import DroneMission, Product
from datetime import datetime
from typing import List

router = APIRouter(prefix="/drones", tags=["Drones"])

# ✅ Auto Dispatch Drone to Deliver a Product
@router.post("/dispatch")
def dispatch_drone(
    product_id: int,
    destination: str,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    mission = DroneMission(
        drone_id="DRONE-AI-AUTO",  # in real case use logic to pick available drone
        product_id=product.id,
        destination=destination,
        status="in-transit",
        eta=datetime.utcnow(),
        initiated_by="system",
        auto_mode=True
    )
    db.add(mission)
    db.commit()
    db.refresh(mission)

    return {"message": "Drone dispatched successfully", "mission_id": mission.id}


# ✅ Get All Active Missions (Live Status)
@router.get("/missions", response_model=List[dict])
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
            "eta": m.eta,
            "auto_mode": m.auto_mode,
            "initiated_by": m.initiated_by
        })

    return output
