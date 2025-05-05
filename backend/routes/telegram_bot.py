from fastapi import APIRouter, Request, HTTPException
from backend.utils.telegram_bot import send_telegram_message

router = APIRouter()

@router.post("/telegram/webhook", summary="🎯 Telegram Bot Webhook")
async def telegram_webhook(request: Request):
    data = await request.json()

    try:
        # Step 1: Extract info
        message = data.get("message", {})
        chat = message.get("chat", {})
        chat_id = str(chat.get("id"))
        text = message.get("text", "")

        if not chat_id or not text:
            raise ValueError("Chat ID or text is missing.")

        # Step 2: Bot logic
        if text.lower() == "/start":
            reply = (
                "👋 *Karibu kwenye SmartBiz Bot!*\n\n"
                "Andika ujumbe wowote ili tuweze kujibu kwa haraka.\n\n"
                "_Unaweza kutumia huduma yetu ya AI kwa kutuma swali lolote kuhusu biashara._"
            )
        elif "asante" in text.lower():
            reply = "🙏 Karibu sana! Kama una swali lingine, tuambie."
        else:
            reply = f"📩 *Umesema:* `{text}`\n\n_Tutakujibu haraka._"

        # Step 3: Tuma majibu kwa Telegram
        await send_telegram_message(chat_id=chat_id, message=reply)

        return {"status": "✅ Webhook received", "chat_id": chat_id}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Webhook error: {str(e)}")
