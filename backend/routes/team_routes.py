from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import TeamMember, User
from backend.schemas import TeamMemberCreate, TeamMemberUpdate, TeamMemberOut
from backend.dependencies import get_current_user
from typing import List

router = APIRouter(prefix="/team", tags=["Team Management"])

# Get team members for current user's business
@router.get("/members", response_model=List[TeamMemberOut])
def get_team_members(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(TeamMember).filter(TeamMember.owner_id == current_user.id).all()

# Add a team member
@router.post("/add", response_model=TeamMemberOut)
def add_team_member(
    payload: TeamMemberCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing = db.query(TeamMember).filter_by(owner_id=current_user.id, email=payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Team member already exists")

    new_member = TeamMember(owner_id=current_user.id, **payload.dict())
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member

# Update a team member
@router.put("/update/{member_id}", response_model=TeamMemberOut)
def update_team_member(
    member_id: int,
    payload: TeamMemberUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    member = db.query(TeamMember).filter_by(id=member_id, owner_id=current_user.id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Team member not found")

    for field, value in payload.dict(exclude_unset=True).items():
        setattr(member, field, value)

    db.commit()
    db.refresh(member)
    return member

# Remove a team member
@router.delete("/remove/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_team_member(
    member_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    member = db.query(TeamMember).filter_by(id=member_id, owner_id=current_user.id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Team member not found")

    db.delete(member)
    db.commit()
    return
