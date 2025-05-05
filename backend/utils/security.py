"""
Security utilities for SmartBiz Assistance SaaS.
Handles password hashing, JWT token encoding, and decoding securely.
"""

import os
from datetime import datetime, timedelta
from typing import Any, Dict

from dotenv import load_dotenv
from jose import JWTError, jwt
from passlib.context import CryptContext

# ==================== LOAD ENVIRONMENT VARIABLES ====================
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("❌ SECRET_KEY not found in environment variables!")

ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

# ==================== PASSWORD HASHING ====================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """
    Hash a plain password using bcrypt.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a provided password against the stored hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)

# ==================== JWT TOKEN CREATION ====================
def create_access_token(data: Dict[str, Any], expires_delta: timedelta = None) -> str:
    """
    Generate a JWT access token with an optional expiration time.
    The 'sub' field should ideally hold user email or ID.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ==================== JWT TOKEN DECODING ====================
def decode_access_token(token: str) -> Dict[str, Any]:
    """
    Decode a JWT token and return the payload.
    Raises ValueError if the token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        raise ValueError(f"❌ Invalid or expired token: {e}") from e
