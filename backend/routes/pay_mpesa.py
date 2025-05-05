"""
Payment routes for SmartBiz Assistant.
Handles M-PESA payment initiation and manual confirmation.
"""

import uuid
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.models import Payment, User
from backend.schemas import PaymentRequest, PaymentResponse, ConfirmMpesaRequest
from backend.auth import get_current_user
from backend.dependencies import check_admin  # hakikisha una hii dependency ya ku-check kama user ni admin

router = APIRouter()

# === M-PESA Configuration ===
PAYBILL_NUMBER = "5261077"
ACCOUNT_NAME = "Ukumbi wa Mjasiriamali"


@router.post(
    "/pay-mpesa",
    response_model=PaymentResponse,
    summary="Initiate M-PESA payment"
)
def initiate_mpesa_payment(
    payload: PaymentRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> PaymentResponse:
    """
    Create a pending payment record and return M-PESA instructions.
    """
    if payload.amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Amount must be greater than 0"
        )

    reference = payload.reference or f"MPESA-{uuid.uuid4().hex[:6].upper()}"

    payment = Payment(
        id=str(uuid.uuid4()),
        user_id=current_user.id,
        method="mpesa",
        amount=payload.amount,
        status="pending",
        phone_number=payload.phone_number,
        created_at=datetime.utcnow(),
        reference=reference
    )

    db.add(payment)
    db.commit()
    db.refresh(payment)

    return PaymentResponse(
        id=payment.id,
        reference=payment.reference,
        amount=payment.amount,
        status=payment.status,
        phone_number=payment.phone_number,
        method=payment.method,
        created_at=payment.created_at,
        instructions=(
            f"Lipa kwa M-PESA:\n"
            f"✅ LIPA NAMBA: {PAYBILL_NUMBER}\n"
            f"✅ Akaunti: {ACCOUNT_NAME}\n"
            f"📌 Kumbukumbu: {payment.reference}"
        )
    )


@router.post(
    "/confirm-mpesa",
    response_model=PaymentResponse,
    summary="✅ Confirm M-PESA payment manually"
)
def confirm_mpesa_payment(
    payload: ConfirmMpesaRequest,
    db: Session = Depends(get_db)
) -> PaymentResponse:
    """
    Manually confirm a pending M-PESA payment by reference code.
    """
    payment = db.query(Payment).filter(Payment.reference == payload.reference).first()

    if not payment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="❌ Payment not found"
        )

    if payment.status.lower() == "confirmed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="⚠️ Payment already confirmed"
        )

    payment.status = "confirmed"
    payment.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(payment)

    return PaymentResponse(
        id=payment.id,
        reference=payment.reference,
        amount=payment.amount,
        status=payment.status,
        phone_number=payment.phone_number,
        method=payment.method,
        created_at=payment.created_at,
        updated_at=payment.updated_at,
        instructions="✅ M-PESA payment confirmed manually."
    )

@router.get("/my-payments", summary="Get my payment history")
def get_my_payments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    payments = db.query(Payment).filter(Payment.user_id == current_user.id).order_by(Payment.created_at.desc()).all()

    return [
        {
            "reference": p.reference,
            "amount": p.amount,
            "status": p.status,
            "method": p.method,
            "phone_number": p.phone_number,
            "created_at": p.created_at.isoformat(),
            "updated_at": p.updated_at.isoformat() if p.updated_at else None,
        }
        for p in payments
    ]


@router.get("/admin/payments", summary="Admin - View all payments")
def get_all_payments_for_admin(
    db: Session = Depends(get_db),
    current_user: User = Depends(check_admin)  # 👈 Only admin can access
):
    payments = db.query(Payment).order_by(Payment.created_at.desc()).all()

    return [
        {
            "reference": p.reference,
            "amount": p.amount,
            "status": p.status,
            "method": p.method,
            "phone_number": p.phone_number,
            "user_id": p.user_id,
            "created_at": p.created_at.isoformat(),
            "updated_at": p.updated_at.isoformat() if p.updated_at else None
        }
        for p in payments
    ]
