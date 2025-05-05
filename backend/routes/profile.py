"""
Routes for managing user profile operations in SmartBiz Assistant.
Includes get, update, and delete functionalities for authenticated users.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.auth import get_current_user
from backend.schemas import UserUpdate, User
from backend.models import User as UserModel  # ✅ Rename User model to UserModel

router = APIRouter()

# ==================== GET CURRENT PROFILE ====================
@router.get("/me", response_model=User, summary="Get current user profile")
def read_current_user(
    current_user: UserModel = Depends(get_current_user)
):
    """
    Retrieve the currently authenticated user's profile details.
    """
    return current_user

# ==================== UPDATE CURRENT PROFILE ====================
@router.put("/me", response_model=User, summary="Update current user profile")
def update_current_user(
    update_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """
    Update the current authenticated user's profile fields.
    """
    # Merge session if detached
    persistent_user = db.merge(current_user)

    # Only update fields provided
    if update_data.full_name is not None:
        persistent_user.full_name = update_data.full_name
    if update_data.business_name is not None:
        persistent_user.business_name = update_data.business_name
    if update_data.business_type is not None:
        persistent_user.business_type = update_data.business_type
    if update_data.language is not None:
        persistent_user.language = update_data.language
    if update_data.telegram_id is not None:
        persistent_user.telegram_id = update_data.telegram_id

    db.commit()
    db.refresh(persistent_user)
    return persistent_user

# ==================== DELETE CURRENT PROFILE ====================
@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT, summary="Delete current user profile")
def delete_current_user(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """
    Delete the current authenticated user's profile completely.
    """
    persistent_user = db.merge(current_user)

    if not persistent_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )

    db.delete(persistent_user)
    db.commit()
    return {"detail": "User deleted successfully"}
