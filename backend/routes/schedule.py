from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.schemas import ScheduledMessageCreate, ScheduledMessageOut
from backend.crud import create_scheduled_message, get_user_scheduled_messages
from backend.models import User

from typing import List
from datetime import datetime  # ✅ Hii ndiyo sahihi kabisa

router = APIRouter(
    prefix="/schedule",
    tags=["Scheduled Promotions"]
)

@router.post("/", response_model=ScheduledMessageOut)
def schedule_message(
    payload: ScheduledMessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_scheduled_message(db, user_id=current_user.id, msg=payload)

@router.get("/", response_model=List[ScheduledMessageOut])
def get_my_scheduled_messages(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_scheduled_messages(db, user_id=current_user.id)
