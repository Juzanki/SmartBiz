"""
Authentication utilities for verifying user credentials, decoding JWT,
and managing current user retrieval from tokens.
"""

from typing import Generator, Optional
from datetime import datetime, timedelta
import os

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from backend.models import User  # ✅ Corrected: Use from models, not schemas
from backend.db import SessionLocal
from backend.routes.logout import verify_not_blacklisted
from backend.crud import get_user_by_email, get_user_by_username, get_user_by_phone
from backend.utils.security import (
    verify_password,
    SECRET_KEY,
    ALGORITHM
)

# ========== Load Environment ==========
load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))  # string default

# ========== OAuth2 Scheme ==========
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ========== Database Session ==========
def get_db() -> Generator:
    """Yield a SQLAlchemy database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ========== Authenticate User ==========
def authenticate_user(db: Session, identifier: str, password: str):
    """Authenticate user using email, username, or phone number."""
    user = (
        get_user_by_email(db, email=identifier.lower())
        or get_user_by_username(db, username=identifier)
        or get_user_by_phone(db, phone_number=identifier)
    )
    if not user or not verify_password(password, user.password):
        return None
    return user

# ========== Create Access Token ==========
def create_access_token(data: dict, expires_delta: timedelta = None):
    """Generate a JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ========== Get Current User ==========
def get_current_user(
    token: str = Depends(verify_not_blacklisted),
    db: Session = Depends(get_db)
) -> User:
    """Decode JWT token and retrieve the current user."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception from e

    user = get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception

    return user

# ========== Check Subscription Status ==========
def check_subscription_status(required_status: list[str]):
    """Ensure the user has the required subscription level."""
    def _check(current_user: User = Depends(get_current_user)):
        if current_user.subscription_status not in required_status:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient subscription level",
            )
        return current_user
    return _check

