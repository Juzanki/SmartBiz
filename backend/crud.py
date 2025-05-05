"""
CRUD operations for SmartBiz Assistance SaaS:
- Users
- API Keys
- Posts
- Settings
- Messages
- Scheduled Messages
"""

from datetime import datetime
from typing import List
from uuid import uuid4

from sqlalchemy.orm import Session

from backend import schemas
from backend.models import User, APIKey, SocialMediaPost, Setting, MessageLog, ScheduledMessage
from backend.utils.security import get_password_hash

# ==================== USER CRUD ====================

def create_user(db: Session, user: schemas.UserCreate) -> User:
    """Create a new user with hashed password."""
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email.lower(),
        full_name=user.full_name,
        phone_number=user.phone_number,
        telegram_id=user.telegram_id,
        business_name=user.business_name,
        business_type=user.business_type,
        language=user.language,
        password=hashed_password,
        subscription_status=user.subscription_status,
        subscription_expiry=user.subscription_expiry
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    """Get list of users ordered by newest."""
    return db.query(User).order_by(User.id.desc()).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int) -> User:
    """Get a user by ID."""
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User:
    """Get a user by email."""
    return db.query(User).filter(User.email == email.lower()).first()

def get_user_by_username(db: Session, username: str) -> User:
    """Get a user by username."""
    return db.query(User).filter(User.username == username).first()

def get_user_by_phone(db: Session, phone_number: str) -> User:
    """Get a user by phone number."""
    return db.query(User).filter(User.phone_number == phone_number).first()

def get_user_by_identifier(db: Session, identifier: str) -> User:
    """Get a user by email, username, or phone."""
    return db.query(User).filter(
        (User.email == identifier.lower()) |
        (User.username == identifier) |
        (User.phone_number == identifier)
    ).first()

def update_user_profile(db: Session, user_id: int, updated_data: schemas.UserUpdate) -> User:
    """Update user's profile information."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    for field, value in updated_data.dict(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user

# ==================== API KEY CRUD ====================

def create_api_key(db: Session, api_data: schemas.APIKeyCreate) -> APIKey:
    """Create a new API Key."""
    new_key = str(uuid4())
    db_key = APIKey(name=api_data.name, key=new_key)
    db.add(db_key)
    db.commit()
    db.refresh(db_key)
    return db_key

def get_api_keys(db: Session) -> List[APIKey]:
    """Get all API keys."""
    return db.query(APIKey).all()

# ==================== POSTS CRUD ====================

def create_post(db: Session, post: schemas.PostCreate) -> SocialMediaPost:
    """Create a new social media post."""
    db_post = SocialMediaPost(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, skip: int = 0, limit: int = 100) -> List[SocialMediaPost]:
    """Get all social media posts."""
    return db.query(SocialMediaPost).offset(skip).limit(limit).all()

def get_user_posts(db: Session, user_id: int) -> List[SocialMediaPost]:
    """Get all posts for a specific user."""
    return db.query(SocialMediaPost).filter(SocialMediaPost.user_id == user_id).all()

# ==================== SETTINGS CRUD ====================

def create_setting(db: Session, setting: schemas.SettingCreate) -> Setting:
    """Create a new app setting."""
    db_setting = Setting(**setting.dict())
    db.add(db_setting)
    db.commit()
    db.refresh(db_setting)
    return db_setting

def get_settings(db: Session) -> List[Setting]:
    """Get all app settings."""
    return db.query(Setting).all()

# ==================== MESSAGE LOG CRUD ====================

def log_message(db: Session, sender_id: str, sender_name: str, content: str, source: str = "telegram") -> MessageLog:
    """Save an incoming message into the log."""
    log_entry = MessageLog(
        sender_id=sender_id,
        sender_name=sender_name,
        content=content,
        source=source,
        timestamp=datetime.utcnow()
    )
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    return log_entry

# ==================== SCHEDULED MESSAGE CRUD ====================

def create_scheduled_message(db: Session, user_id: int, msg: schemas.ScheduledMessageCreate) -> ScheduledMessage:
    """Schedule a new message for later sending."""
    new_msg = ScheduledMessage(**msg.dict(), user_id=user_id)
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return new_msg

def get_user_scheduled_messages(db: Session, user_id: int) -> List[ScheduledMessage]:
    """Get all scheduled messages for a user."""
    return db.query(ScheduledMessage).filter(ScheduledMessage.user_id == user_id).order_by(ScheduledMessage.scheduled_time.desc()).all()

def get_due_unsent_messages(db: Session) -> List[ScheduledMessage]:
    """Get all unsent messages that are due."""
    now = datetime.utcnow()
    return db.query(ScheduledMessage).filter(ScheduledMessage.sent == False, ScheduledMessage.scheduled_time <= now).all()

def mark_as_sent(db: Session, msg: ScheduledMessage):
    """Mark a scheduled message as sent."""
    msg.sent = True
    db.commit()
    db.refresh(msg)
