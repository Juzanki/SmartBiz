from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from backend.db import get_db
from backend.models import Campaign, Product, User
from backend.schemas import CampaignCreate
from backend.dependencies import get_current_user

router = APIRouter(prefix="/campaigns", tags=["Campaigns"])

@router.post("/create")
def create_campaign(
    payload: CampaignCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == payload.product_id).first()
    if not product or product.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Invalid product or permission denied")

    ends_at = datetime.utcnow() + timedelta(days=payload.duration)

    campaign = Campaign(
        title=payload.title,
        product_id=payload.product_id,
        owner_id=current_user.id,
        commission_rate=payload.rate,
        ends_at=ends_at
    )
    db.add(campaign)
    db.commit()
    db.refresh(campaign)
    return {"message": "Campaign created", "id": campaign.id}
