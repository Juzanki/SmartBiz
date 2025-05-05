from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import SupportTicket, User
from backend.schemas import SupportTicketOut
from backend.dependencies import get_current_user
from typing import List

router = APIRouter(prefix="/admin/support", tags=["Admin Support"])

# View all tickets (admin only)
@router.get("/", response_model=List[SupportTicketOut])
def get_all_tickets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != 'admin' and current_user.role != 'owner':
        raise HTTPException(status_code=403, detail="Not authorized")
    return db.query(SupportTicket).order_by(SupportTicket.created_at.desc()).all()

# Close a ticket
@router.put("/close/{ticket_id}", status_code=status.HTTP_200_OK)
def close_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != 'admin' and current_user.role != 'owner':
        raise HTTPException(status_code=403, detail="Not authorized")

    ticket = db.query(SupportTicket).filter(SupportTicket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    ticket.status = "closed"
    db.commit()
    return {"message": "Ticket closed"}
