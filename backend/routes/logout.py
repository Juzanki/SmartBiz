"""
Logout endpoint for SmartBiz Assistant.
Handles logging out users by blacklisting JWT tokens in memory.
"""

from datetime import datetime
from typing import Set

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from backend.utils.security import SECRET_KEY, ALGORITHM

router = APIRouter()

# ========== In-memory Token Blacklist ==========
blacklisted_tokens: Set[str] = set()

# OAuth2 Scheme for token extraction
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/", summary="Logout and invalidate current token")
def logout_user(token: str = Depends(oauth2_scheme)):

    """
    Invalidate the current user's JWT token by adding it to a temporary blacklist.
    Returns a success message if the token is valid and added to the blacklist.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        exp = payload.get("exp")

        if not exp:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token missing expiry"
            )

        if datetime.utcnow().timestamp() > exp:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has already expired"
            )

        blacklisted_tokens.add(token)
        return {"message": "✅ Logout successful"}

    except JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        ) from exc


def verify_not_blacklisted(token: str = Depends(oauth2_scheme)) -> str:
    """
    Dependency to reject blacklisted tokens.
    Should be used in get_current_user to block access for logged-out sessions.
    """
    if token in blacklisted_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has been logged out"
        )
    return token
