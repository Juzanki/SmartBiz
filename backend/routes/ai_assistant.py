# backend/routes/ai_assistant.py

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from backend.dependencies import get_current_user
from backend.models import User
import openai
import os

router = APIRouter(prefix="/ai-assistant", tags=["AI Assistant"])

# Load API Key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

class AIAssistantRequest(BaseModel):
    prompt: str
    language: str = "sw"  # default Kiswahili, but supports any language

@router.post("/ask", summary="Tuma ombi kwa AI Assistant")
async def ask_ai(request: AIAssistantRequest, current_user: User = Depends(get_current_user)):
    try:
        prompt = f"You are a Smart Business Assistant. Language: {request.language}.\nUser: {current_user.email}\nTask: {request.prompt}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800
        )
        reply = response.choices[0].message.content
        return {
            "user": current_user.email,
            "task": request.prompt,
            "assistant_reply": reply
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Assistant Error: {str(e)}")
