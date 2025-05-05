from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/nfc/{nfc_id}", summary="Handle NFC tag scan")
def read_nfc(nfc_id: str):
    # Future: NFC mapping to product
    return {
        "message": "NFC feature in preview mode",
        "nfc_id": nfc_id,
        "next_step": "Scan successful, show product details"
    }
