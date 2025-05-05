from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models import MessageLog, User
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/inbox", tags=["Inbox"])

class MessageOut(BaseModel):
    id: int
    sender_name: str
    message: str
    platform: str
    chat_id: str
    received_at: datetime

    class Config:
        orm_mode = True

@router.get("/", response_model=List[MessageOut])
def get_all_messages(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role in ['admin', 'owner']:
        return db.query(MessageLog).order_by(MessageLog.received_at.desc()).all()
    return db.query(MessageLog).filter(MessageLog.chat_id == str(current_user.id)).all()
