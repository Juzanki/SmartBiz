from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.auth import get_current_user
from backend.db import get_db
from backend.models import User
from backend.schemas import BroadcastMessage
from backend.dependencies import check_admin
from backend.schemas import CampaignRequest
from backend.utils.telegram_bot import send_telegram_message
# future: from backend.utils.whatsapp_bot import send_whatsapp_message
# future: from backend.utils.sms_gateway import send_sms

router = APIRouter()

@router.post("/broadcast", summary="📢 Send broadcast message to all users")
async def broadcast_message(
    payload: BroadcastMessage,
    db: Session = Depends(get_db),
    current_user: User = Depends(check_admin)
):
    users = db.query(User).all()
    sent_count = 0

    for user in users:
        if "telegram" in payload.channels and user.telegram_id:
            await send_telegram_message(user.telegram_id, payload.message)
            sent_count += 1

        # if "whatsapp" in payload.channels and user.phone_number:
        #     await send_whatsapp_message(user.phone_number, payload.message)

        # if "sms" in payload.channels and user.phone_number:
        #     await send_sms(user.phone_number, payload.message)

    return {
        "message": "✅ Broadcast sent",
        "total_users": len(users),
        "messages_sent": sent_count
    }
