from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from backend.db import get_db
from backend.models import User
from backend.dependencies import get_current_user
from sqlalchemy.orm import Session
import openai  # or your local LLM integration

router = APIRouter(prefix="/owner", tags=["Owner AI Console"])

class AICommandRequest(BaseModel):
    prompt: str

@router.post("/command")
def execute_owner_command(
    body: AICommandRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "owner":
        raise HTTPException(status_code=403, detail="Access restricted to owner only")

    prompt = body.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Command prompt is required")

    # Example OpenAI usage (can be replaced with a local LLM call)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a backend assistant with admin privileges."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        reply = response.choices[0].message.content.strip()
        return {"message": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI error: {str(e)}")
