import os
from typing import List
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from backend.routes.order_notification import router as order_notification_router  # Single import

# ========== LOCAL MODULES ========== 
from backend.models import Base
from backend.schemas import UserCreate, User as UserResponse
from backend.crud import get_user, create_user, get_users
from backend.db import SessionLocal, engine
from backend.auth_routes import router as auth_router
from backend.routes import settings_routes, orders_routes, live_stream
from backend.routes import (
    register, auth_routes, logout, profile, forgot_password, pay_mpesa,
    ai_responder, admin_routes, subscription, telegram_bot, broadcast,
    negotiation_bot, voice_assistant, qr_generator, nfc_handler, qr_orders,
    qr_code, nfc_orders, smart_orders, platforms, language, messages, inbox,
    reply, schedule
)
from backend.routes.owner_routes import owner_router
from backend.middleware.language import language_middleware
from backend.tasks.scheduler import run_scheduled_task
from backend.routes.invoice import router as invoice_router


# ========== SCHEDULER SETUP ========== 
scheduler = BackgroundScheduler()

# Task to execute scheduled posts
def send_scheduled_posts():
    logging.info("Scheduled posts sent")  # Logging to track posts

# Add job to scheduler
scheduler.add_job(send_scheduled_posts, 'interval', minutes=1)

# Start scheduler
scheduler.start()


# ========== APP INIT ========== 
app = FastAPI(
    title="SmartBiz Assistant API",
    description="Powerful SaaS backend for automating business operations",
    version="1.0.0"
)

# ========== LOGGING ========== 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ========== CORS MIDDLEWARE ========== 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Dev only, for production set appropriate origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== ENV VARIABLES ========== 
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID", "")
RECIPIENT_PHONE = os.getenv("RECIPIENT_PHONE", "")

# ========== DATABASE SETUP ========== 
Base.metadata.create_all(bind=engine)

# ========== DB DEPENDENCY ========== 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ========== ROUTES ========== 
app.include_router(auth_router, tags=["Auth"])
app.include_router(register.router, prefix="/register-user", tags=["Register"])
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth-Routes"])
app.include_router(logout.router, prefix="/logout", tags=["Logout"])
app.include_router(profile.router, tags=["Profile"])
app.include_router(forgot_password.router, prefix="/forgot-password", tags=["Forgot-Password"])
app.include_router(pay_mpesa.router, tags=["Payments"])
app.include_router(admin_routes.router)
app.include_router(ai_responder.router)
app.include_router(subscription.router, prefix="/subscriptions", tags=["Subscriptions"])
app.include_router(telegram_bot.router, prefix="/telegram", tags=["Telegram"])
app.include_router(broadcast.router, prefix="/admin", tags=["Broadcast"])
app.include_router(negotiation_bot.router, tags=["AI Negotiation"])
app.include_router(voice_assistant.router, prefix="/assistant", tags=["Voice Assistant"])
app.include_router(owner_router, prefix="/owner", tags=["Owner Panel"])
app.include_router(qr_generator.router, prefix="/qr", tags=["QR"])
app.include_router(nfc_handler.router, prefix="/nfc", tags=["NFC"])
app.include_router(qr_orders.router, prefix="/orders", tags=["Smart Orders"])
app.include_router(qr_code.router, prefix="/qr", tags=["QR Codes"])
app.include_router(nfc_orders.router, prefix="/nfc", tags=["NFC"])
app.include_router(smart_orders.router, prefix="/smart-orders", tags=["Smart Orders"])
app.include_router(order_notification_router, tags=["Order Notification"])  # Correct import
app.include_router(platforms.router)
app.include_router(language.router, prefix="/user", tags=["Language"])
app.add_middleware(language_middleware)
app.include_router(messages.router)
app.include_router(inbox.router)
app.include_router(reply.router)
app.include_router(schedule.router)
app.include_router(settings_routes.router)
app.include_router(orders_routes.router)
app.include_router(live_stream.router)
app.include_router(invoice_router)

# ========== SCHEDULED TASKS ========== 
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_scheduled_task())

# ========== ROOT ========== 
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "✅ Welcome to SmartBiz Assistant API",
        "docs": "/docs",
        "status": "running"
    }

# ========== USER MANAGEMENT ========== 
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@app.get("/users/", response_model=List[UserResponse], tags=["Users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# ========== WHATSAPP PLACEHOLDER ========== 
class WhatsAppMessage(BaseModel):
    message: str

@app.post("/send-whatsapp/", tags=["WhatsApp"])
async def send_whatsapp_message(message: WhatsAppMessage):
    return {
        "status": "queued",
        "to": RECIPIENT_PHONE or "N/A",
        "message": message.message
    }

# ========== RUN SERVER ========== 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
