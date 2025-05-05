from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import User, ReferralLog
from datetime import datetime

router = APIRouter(tags=["Referral Tracker"])

@router.get("/ref/{username}")
def track_referral(username: str, request: Request, db: Session = Depends(get_db)):
    ref_user = db.query(User).filter(User.username == username).first()
    if not ref_user:
        return {"message": "Invalid referral link"}

    # Store referral cookie for tracking
    response = {"message": f"Referral from @{username} recorded"}
    request.session["ref_by"] = username
    return response

# Usage in purchase logic:
# if "ref_by" in session:
#     create ReferralLog entry during checkout
