# backend/routes/platforms.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models import ConnectedPlatform
from backend.schemas import PlatformConnectRequest, PlatformOut
from backend.models import User

router = APIRouter(prefix="/platforms", tags=["Integrations"])

@router.post("/connect", response_model=PlatformOut)
def connect_platform(payload: PlatformConnectRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    platform = ConnectedPlatform(
        user_id=current_user.id,
        platform=payload.platform.lower(),
        access_token=payload.access_token
    )
    db.add(platform)
    db.commit()
    db.refresh(platform)
    return platform

@router.get("/", response_model=list[PlatformOut])
def list_connected_platforms(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(ConnectedPlatform).filter_by(user_id=current_user.id).all()
