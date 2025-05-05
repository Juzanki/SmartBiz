from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models import User

from backend.utils.telegram_bot import send_telegram_message
from backend.utils.whatsapp import send_whatsapp_message
from backend.utils.sms import send_sms_message

router = APIRouter(tags=["Replies"])

class ReplyRequest(BaseModel):
    chat_id: str
    platform: str  # telegram, whatsapp, sms
    message: str

@router.post("/send-reply")
def send_reply(payload: ReplyRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if payload.platform == "telegram":
        res = send_telegram_message(chat_id=payload.chat_id, message=payload.message)
    elif payload.platform == "whatsapp":
        res = send_whatsapp_message(phone=payload.chat_id, message=payload.message)
    elif payload.platform == "sms":
        res = send_sms_message(phone=payload.chat_id, message=payload.message)
    else:
        raise HTTPException(status_code=400, detail="Unsupported platform")

    return {"message": "Reply sent", "result": res}
