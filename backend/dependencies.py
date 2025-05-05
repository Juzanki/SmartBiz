import os
import jwt
import logging
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.models import User
from backend.db import get_db
from backend.auth import get_current_user

# Setup logger
logger = logging.getLogger(__name__)

# ✅ Subscription checker with allowed plans
def require_plan(allowed_plans: list):
    """
    Check if user has a valid subscription plan from allowed_plans.
    """
    def checker(user: User = Depends(get_current_user)):
        if not user.subscription_status or user.subscription_status not in allowed_plans:
            logger.warning(f"❌ Plan Access Denied for: {user.email} - Plan: {user.subscription_status}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="⛔ Access denied: Please upgrade your plan to access this feature."
            )
        logger.info(f"✅ Plan Access Granted: {user.email} - Plan: {user.subscription_status}")
        return user
    return checker

# ✅ Admin checker
def check_admin(current_user: User = Depends(get_current_user)):
    """
    Check if the current user has admin privileges.
    """
    if current_user.role != "admin":
        logger.warning(f"🚫 Unauthorized Admin Attempt: {current_user.email} - Role: {current_user.role}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="⛔ Admin access required."
        )
    logger.info(f"✅ Admin Access Granted: {current_user.email}")
    return current_user

def check_owner_only(current_user: User = Depends(get_current_user)):
    if current_user.role != "owner":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="⛔ Owner access only"
        )
    return current_user


# JWT setup
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == payload.get("sub")).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

def get_current_active_owner(current_user=Depends(get_current_user)):
    if current_user.role != "owner":
        raise HTTPException(status_code=403, detail="Only owner can access")
    return current_user