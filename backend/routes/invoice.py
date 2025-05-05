from fastapi import APIRouter, HTTPException
from backend.services.pdf_service import send_invoice

router = APIRouter()

@router.post("/generate-invoice")
def generate_invoice():
    try:
        payload = {
            "template": {"id": "your_template_id"},
            "data": {
                "name": "Julius Zakayo",
                "amount": "15000",
                "description": "Business Support Plan"
            }
        }
        result = send_invoice(payload)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
