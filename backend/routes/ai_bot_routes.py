from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import AIBotSettings, User
from backend.schemas import AIBotSettingsSchema
from backend.dependencies import get_current_user

router = APIRouter(prefix="/ai-bot", tags=["AI Bot"])

@router.get("/settings", response_model=AIBotSettingsSchema)
def get_ai_bot_settings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    settings = db.query(AIBotSettings).filter(AIBotSettings.user_id == current_user.id).first()
    if not settings:
        raise HTTPException(status_code=404, detail="No settings found")
    return settings


@router.put("/settings", response_model=AIBotSettingsSchema)
def update_ai_bot_settings(
    payload: AIBotSettingsSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    settings = db.query(AIBotSettings).filter(AIBotSettings.user_id == current_user.id).first()
    if settings:
        for key, value in payload.dict().items():
            setattr(settings, key, value)
    else:
        settings = AIBotSettings(user_id=current_user.id, **payload.dict())
        db.add(settings)
    db.commit()
    db.refresh(settings)
    return settings
