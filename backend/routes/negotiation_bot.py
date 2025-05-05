from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.auth import get_current_user
from backend.db import get_db
from backend.models import User
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()

class NegotiationRequest(BaseModel):
    product_name: str
    initial_price: float
    message: str

@router.post("/negotiate", summary="Negotiate with AI Bot")
def negotiate_price(
    request: NegotiationRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    prompt = (
        f"Customer is interested in buying '{request.product_name}' priced at {request.initial_price} TZS.\n"
        f"Customer message: {request.message}\n"
        f"Act like a smart negotiation bot and give a polite and helpful response."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content.strip()
        return {
            "product": request.product_name,
            "initial_price": request.initial_price,
            "user_message": request.message,
            "bot_response": reply
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Negotiation bot failed: {str(e)}")
