"""
Route to handle business user registration in SmartBiz Assistant.
Ensures unique phone and Telegram ID before saving new user entry.
"""

from uuid import uuid4
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.models import User
from backend.utils.security import get_password_hash

router = APIRouter()

class RegisterRequest(BaseModel):
    """Schema for user registration input."""
    username: str
    email: str
    password: str
    phone_number: str
    full_name: Optional[str] = "Guest"
    business_name: str
    business_type: str
    language: str
    telegram_id: Optional[int] = None


class RegisterResponse(BaseModel):
    """Schema for response after registration."""
    user_token: str
    message: str


@router.post("/register-user", response_model=RegisterResponse, summary="Register a new user")
def register_user(data: RegisterRequest, db: Session = Depends(get_db)):
    """
    Register a new business user with unique phone number and Telegram ID.
    """
    if data.telegram_id:
        existing = db.query(User).filter_by(telegram_id=data.telegram_id).first()
        if existing:
            raise HTTPException(status_code=400, detail="User already registered.")

    existing_phone = db.query(User).filter_by(phone_number=data.phone_number).first()
    if existing_phone:
        raise HTTPException(status_code=400, detail="Phone number already registered.")

    token = str(uuid4())

    new_user = User(
        username=data.username,
        email=data.email,
        full_name=data.full_name or "Guest User",
        password=get_password_hash(data.password),
        telegram_id=data.telegram_id,
        business_name=data.business_name,
        business_type=data.business_type,
        language=data.language,
        phone_number=data.phone_number,
        user_token=token,
        subscription_status="free",
        subscription_expiry=datetime.utcnow(),
        created_at=datetime.utcnow()
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return RegisterResponse(
            user_token=token,
            message="Business registered successfully."
        )
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Registration failed due to server error."
        ) from exc
