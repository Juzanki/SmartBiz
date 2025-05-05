from fastapi import APIRouter
import qrcode
import base64
from fastapi.responses import StreamingResponse
from io import BytesIO

router = APIRouter()

@router.get("/generate-qr/{product_id}", summary="Generate QR for product")
def generate_qr(product_id: int):
    url = f"https://yourdomain.com/product/{product_id}"
    qr = qrcode.make(url)
    buf = BytesIO()
    qr.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")

def generate_product_qr(data: str) -> str:
    """
    Generates a base64-encoded QR code image from the given data string.
    """
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")