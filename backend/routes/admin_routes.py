from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas import UserUpdate, User, PaymentResponse
from backend.db import get_db
from backend.models import Payment, User as UserModel
from backend.dependencies import check_admin

router = APIRouter()

# ====================== VIEW ALL PAYMENTS ======================
@router.get("/admin/payments", response_model=list[PaymentResponse], summary="🔐 Admin: View all payments")
def admin_get_all_payments(db: Session = Depends(get_db), current_user=Depends(check_admin)):
    payments = db.query(Payment).order_by(Payment.created_at.desc()).all()
    return payments

# ====================== VIEW ALL USERS ======================
@router.get("/admin/users", response_model=list[User], summary="🔐 Admin: View all users", dependencies=[Depends(check_admin)])
def admin_view_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).order_by(UserModel.created_at.desc()).all()
    return users

# ====================== GET SINGLE USER ======================
@router.get("/admin/users/{user_id}", response_model=User, summary="🔐 Admin: Get single user", dependencies=[Depends(check_admin)])
def admin_get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ====================== UPDATE USER ======================
@router.put("/admin/users/{user_id}", response_model=User, summary="🔐 Admin: Update user info", dependencies=[Depends(check_admin)])
def admin_update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

# ====================== DELETE USER ======================
@router.delete("/admin/users/{user_id}", summary="🔐 Admin: Delete user", dependencies=[Depends(check_admin)])
def admin_delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": f"✅ User {user_id} deleted successfully."}
