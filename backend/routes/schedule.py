from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from backend.db import get_db
from backend.auth import get_current_user
from backend.schemas import ScheduledMessageCreate, ScheduledMessageOut
from backend.crud.user_crud import (
    create_scheduled_message,
    get_user_scheduled_messages
)
from backend.models import User

router = APIRouter(
    prefix="/schedule",
    tags=["Scheduled Promotions"]
)


# ================== Schedule New Message ==================
@router.post("/", response_model=ScheduledMessageOut, status_code=status.HTTP_201_CREATED, summary="🕒 Schedule new promotional message")
def schedule_message(
    payload: ScheduledMessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a new scheduled message that will be sent later.
    Requires authentication. Supports SMS, WhatsApp, Telegram, etc.
    """
    if payload.send_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Send time must be in the future.")

    return create_scheduled_message(db, user_id=current_user.id, msg=payload)


# ================== Get All Scheduled Messages ==================
@router.get("/", response_model=List[ScheduledMessageOut], summary="📋 List your scheduled messages")
def get_my_scheduled_messages(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Fetch all upcoming or previously scheduled messages for the authenticated user.
    """
    return get_user_scheduled_messages(db, user_id=current_user.id)
