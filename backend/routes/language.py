from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models import User
from backend.schemas import LanguagePreferenceUpdate

router = APIRouter()

@router.put("/language", summary="Update language preference")
def update_language(
    payload: LanguagePreferenceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    current_user.language = payload.language
    db.commit()
    db.refresh(current_user)
    return {"message": f"Language updated to {payload.language}"}
