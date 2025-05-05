import logging
import openai
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
)

# ===================== ENVIRONMENT SETUP =====================
load_dotenv()  # Load variables from .env file

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# ===================== LOGGING =====================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ===================== COMMAND: /start =====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Karibu SmartBiz Assistant Bot!\n\n"
        "Tuma ujumbe wowote na nitakujibu papo hapo kwa msaada wa AI. 😊"
    )

# ===================== MESSAGE HANDLER =====================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Unaweza kubadilisha kuwa "gpt-4" kama una access
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        bot_reply = response['choices'][0]['message']['content'].strip()
        await update.message.reply_text(bot_reply)

    except Exception as e:
        logging.error("OpenAI Error: %s", str(e))
        await update.message.reply_text("😔 Samahani, kuna tatizo kwa sasa. Jaribu tena baadae.")

# ===================== MAIN =====================
if __name__ == '__main__':
    if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
        raise ValueError("❌ TELEGRAM_TOKEN au OPENAI_API_KEY haijawekwa kwenye .env file!")

    print("✅ SmartBiz Bot inafanya kazi...")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
