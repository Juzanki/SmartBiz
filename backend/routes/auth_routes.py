"""
Auth Routes for SmartBiz Assistant.
Handles login, registration, password reset and session verification.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from backend.db import get_db
from backend.models import User
from backend.utils.security import verify_password, get_password_hash
from backend.auth import create_access_token, get_current_user

router = APIRouter()

# ==================== Schemas ====================
class LoginOutput(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict

class RegisterInput(BaseModel):
    username: str
    email: EmailStr
    phone_number: str
    full_name: str
    password: str

class MeResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone_number: str
    subscription_status: str

# ==================== Routes ====================
@router.post("/login", response_model=LoginOutput, summary="Login using email, phone or username")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Authenticate user and return JWT token."""
    # Identify user by email, username, or phone_number
    user = db.query(User).filter(
        (User.email == form_data.username) |
        (User.username == form_data.username) |
        (User.phone_number == form_data.username)
    ).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.email})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "full_name": user.full_name,
            "role": user.role,
            "language": user.language,
            "subscription_status": user.subscription_status,
        }
    }

@router.post("/register", summary="Register a new user")
def register(data: RegisterInput, db: Session = Depends(get_db)):
    """Register new user account and return success message."""
    existing = db.query(User).filter((User.email == data.email) | (User.username == data.username)).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        username=data.username,
        email=data.email,
        phone_number=data.phone_number,
        full_name=data.full_name,
        password=get_password_hash(data.password),
        subscription_status="free"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Registration successful"}

@router.get("/me", response_model=MeResponse, summary="Get current user profile")
def get_profile(current_user: User = Depends(get_current_user)):
    """Return profile of the currently logged-in user."""
    return current_user
