import asyncio
from datetime import datetime  # ✅ Hii ni muhimu kama inatumika ndani ya CRUD

from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.crud import get_due_unsent_messages, mark_as_sent
from backend.utils.telegram_bot import send_telegram_message
from backend.utils.whatsapp import send_whatsapp_message
from backend.utils.sms import send_sms_message

async def run_scheduled_task():
    while True:
        try:
            db: Session = SessionLocal()
            due_messages = get_due_unsent_messages(db)

            for msg in due_messages:
                # Send via correct platform
                if msg.platform == "telegram":
                    send_telegram_message(msg.recipient, msg.message)
                elif msg.platform == "whatsapp":
                    send_whatsapp_message(msg.recipient, msg.message)
                elif msg.platform == "sms":
                    send_sms_message(msg.recipient, msg.message)

                mark_as_sent(db, msg)

            db.close()
        except Exception as e:
            print(f"[Scheduler error]: {e}")

        await asyncio.sleep(60)  # Check every 60 seconds
