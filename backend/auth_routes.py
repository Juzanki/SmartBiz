"""
Authentication & User Management Routes
Includes signup, login, profile update, post creation, subscription-based features.
"""

import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.dependencies import require_plan
from backend.schemas import PostCreate, PostOut, UserCreate, UserUpdate, User, Token
from backend.crud import (
    get_user_by_email,
    create_user,
    update_user_profile,
    create_post as crud_create_post,
    get_user_posts,
)
from backend.auth import (
    get_current_user,
    authenticate_user,
    get_db,
)
from backend.utils.security import (
    get_password_hash,
    create_access_token,
)

router = APIRouter()
logging.basicConfig(level=logging.INFO)

# ========== CURRENT USER PROFILE ==========
@router.get("/auth/me", response_model=User)
def get_my_profile(current_user: User = Depends(get_current_user)):
    """
    Retrieve the current authenticated user's profile.
    """
    return current_user

# ========== USER SIGNUP ==========
@router.post("/auth/signup", response_model=User, status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user account.
    """
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    
    user.password = get_password_hash(user.password)
    return create_user(db=db, user=user)

# ========== USER LOGIN ==========
@router.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Authenticate user and return JWT token + role + language + name.
    """
    identifier = form_data.username.strip().lower()
    logging.info("🔐 Login attempt with identifier: %s", identifier)

    user = authenticate_user(db, identifier=identifier, password=form_data.password)
    if not user:
        logging.warning("❌ Invalid login for: %s", identifier)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. Please check your email/username/phone and password.",
        )
    
    # Create token
    access_token = create_access_token(data={"sub": user.email})
    logging.info("✅ Successful login for: %s", user.email)

    # Return full response with extra user info
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role,                   # 🔥 Important for role-based routing
        "name": user.full_name or user.username,
        "language": user.language or "en"
    }

# ========== UPDATE PROFILE ==========
@router.put("/auth/update-profile", response_model=User)
def update_profile(
    updated_user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update current user's profile details.
    """
    return update_user_profile(db=db, user_id=current_user.id, updated_data=updated_user)

# ========== CREATE POST (Pro/Business Users Only) ==========
@router.post("/auth/create-post", response_model=PostOut)
def create_post(
    post_data: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_plan(["Pro", "Business"]))
):
    """
    Create a new post (only for Pro or Business plans).
    """
    return crud_create_post(db, post_data)

# ========== GET USER POSTS ==========
@router.get("/auth/my-posts", response_model=List[PostOut])
def list_my_posts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    List all posts created by the current user.
    """
    return get_user_posts(db=db, user_id=current_user.id)

# ========== ACCESS PREMIUM CHATBOT ==========
@router.get("/auth/pro-chatbot")
def premium_chatbot_feature(current_user: User = Depends(require_plan(["Pro", "Business"]))):
    """
    Premium chatbot feature for Pro/Business subscribers.
    """
    return {
        "message": f"Karibu {current_user.full_name}, welcome to the AI Premium Chatbot!",
        "feature": "Smart AI Auto-Responder"
    }

# ========== ACCESS FREE FEATURE ==========
@router.get("/auth/free-feature")
def free_feature(current_user: User = Depends(require_plan(["Free", "Pro", "Business"]))):
    """
    Free feature accessible to all subscription levels.
    """
    return {
        "message": f"Hi {current_user.full_name}, enjoy this free feature available for everyone!"
    }
