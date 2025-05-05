from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from backend.db import get_db
from backend.auth import get_current_user
from backend.models import User

router = APIRouter()

# ==================== SCHEMAS ====================

class SubscriptionPlan(BaseModel):
    id: int
    name: str
    price: int
    duration_days: int
    features: str

class PurchaseRequest(BaseModel):
    plan_name: str

# ==================== STATIC PLAN DATA ====================

PLANS = [
    SubscriptionPlan(
        id=1,
        name="Pro",
        price=30000,
        duration_days=30,
        features="Access to AI Bot, Smart Scheduling, Premium Support"
    ),
    SubscriptionPlan(
        id=2,
        name="Business",
        price=65000,
        duration_days=30,
        features="Everything in Pro + Team Access + Insights"
    ),
    SubscriptionPlan(
        id=3,
        name="Enterprise",
        price=125000,
        duration_days=30,
        features="Unlimited Access, White-labeling, Enterprise Integrations"
    )
]

# ✅ Create dict from plans
plans_dict = {plan.name: plan for plan in PLANS}

# ==================== ROUTES ====================

@router.get("/plans", response_model=list[SubscriptionPlan], summary="📦 View all subscription plans")
def get_subscription_plans():
    return PLANS

@router.post("/purchase")
def purchase_plan(
    purchase: PurchaseRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    plan = plans_dict.get(purchase.plan_name)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")

    # 🛠️ Merge ili instance iwe persistent ndani ya session
    persistent_user = db.merge(current_user)

    persistent_user.subscription_status = purchase.plan_name
    persistent_user.subscription_expiry = datetime.utcnow() + timedelta(days=plan.duration_days)

    db.commit()
    db.refresh(persistent_user)

    return {
        "message": f"✅ Successfully subscribed to {purchase.plan_name}",
        "expires": persistent_user.subscription_expiry.strftime("%Y-%m-%d %H:%M:%S")
    }
