"""
AI Auto Responder Endpoint for SmartBiz Assistant.

Handles AI-powered responses using OpenAI API.
Access is restricted to users with 'Pro' or 'Business' subscription plans.
"""

import os
import logging
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from backend.auth import get_current_user
from backend.models import User
from backend.utils.access_control import require_plan

# ========== Setup ==========
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Logger setup
logger = logging.getLogger(__name__)

router = APIRouter()

# ========== Request Schema ==========
class PromptRequest(BaseModel):
    prompt: str

# ========== AI Responder Endpoint ==========
@router.post(
    "/ai/respond",
    summary="Respond to user prompt using OpenAI",
    dependencies=[Depends(require_plan(["Pro", "Business"]))],
)
def auto_reply_bot(
    request: PromptRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Generate AI response based on user prompt.
    Only accessible to Pro or Business subscribers.
    """
    prompt = request.prompt.strip()

    if not prompt:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Prompt cannot be empty"
        )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content.strip()

        return {
            "user": current_user.email,
            "plan": current_user.subscription_status,
            "prompt": prompt,
            "response": answer
        }

    except Exception as exc:
        logger.exception("❌ OpenAI Error: %s", str(exc))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="OpenAI API Error. Please check your API key and request format."
        ) from exc

# ========== Pro Chatbot Access Test ==========
@router.get("/pro-chatbot", summary="🤖 AI Auto-Responder (Pro/Business only)")
def use_pro_feature(current_user: User = Depends(require_plan(["Pro", "Business"]))):
    return {
        "message": f"✅ Welcome {current_user.full_name}, you are accessing Pro features.",
        "feature": "AI Auto-Responder for Business"
    }
