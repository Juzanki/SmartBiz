"""
SQLAlchemy models for SmartBiz SaaS system.
Defines Users, API Keys, Social Media Posts, Payments, Subscription Plans, and Settings.
"""

import uuid
from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, DateTime, Float,
    ForeignKey, Boolean, func, UniqueConstraint, text
)
from sqlalchemy.orm import relationship
from backend.db import Base
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import JSON


created_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
language = Column(String(10), default="sw", nullable=False)
platform = Column(String)  # telegram, whatsapp, sms
nfc_tag = Column(String, unique=True, nullable=True)
platforms = relationship("ConnectedPlatform", back_populates="user", cascade="all, delete-orphan")




# ==================== USER MODEL ====================
class User(Base):
    """User account and business profile data."""
    __tablename__ = "users"


    # Relationships
    posts = relationship("SocialMediaPost", back_populates="user", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="user", cascade="all, delete-orphan")
    subscriptions = relationship("UserSubscription", back_populates="user", cascade="all, delete-orphan")
    platforms = relationship("ConnectedPlatform", back_populates="user", cascade="all, delete-orphan")  # 👈 Hii ndo ilikuwa haipo
    products = relationship("Product", back_populates="vendor", cascade="all, delete-orphan")
    scheduled_messages = relationship("ScheduledMessage", back_populates="user", cascade="all, delete-orphan")
    settings = relationship("Settings", back_populates="user", uselist=False)
    joined_campaigns = relationship("CampaignAffiliate", back_populates="user", cascade="all, delete-orphan")
    referrals = relationship("ReferralLog", back_populates="promoter", cascade="all, delete-orphan")
    live_sessions = relationship("LiveSession", back_populates="user", cascade="all, delete-orphan")
    ai_bot_settings = relationship("AIBotSettings", back_populates="user", uselist=False)
    support_tickets = relationship("SupportTicket", back_populates="user", cascade="all, delete-orphan")
    audit_logs = relationship("AuditLog", back_populates="user", cascade="all, delete-orphan")
  





    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, default="user")  # Options: user, admin, owner
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone_number = Column(String(20), unique=True, index=True, nullable=True)
    telegram_id = Column(Integer, unique=True, nullable=True)
    business_name = Column(String(100), nullable=True)
    business_type = Column(String(100), nullable=True)
    language = Column(String(10), default="sw", nullable=False)
    user_token = Column(
        String(100),
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4())
    )
    subscription_status = Column(String(50), default="free", nullable=False)
    subscription_expiry = Column(DateTime(timezone=True), nullable=True)
    full_name = Column(String(100), nullable=True)
    password = Column(String(255), nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        server_default=func.now()  # ✅ Corrected: add parentheses
    )

    posts = relationship(
        "SocialMediaPost",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    payments = relationship(
        "Payment",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    subscriptions = relationship(
        "UserSubscription",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"<User(username='{self.username}', "
            f"email='{self.email}')>"
        )

    def is_subscription_active(self):
        """Check if the user's current subscription is active."""
        if self.subscription_expiry:
            return datetime.utcnow() < self.subscription_expiry
        return False

    def update_subscription(self, plan_name, expiry_date):
        """Update user's subscription plan and expiry date."""
        self.subscription_status = plan_name
        self.subscription_expiry = expiry_date

    @property
    def active_plan_name(self):
        """Get name of the currently active plan."""
        active_plans = [sub for sub in self.subscriptions if sub.is_active]
        if active_plans:
            return active_plans[0].plan.name
        return "Free"
class ConnectedPlatform(Base):
    __tablename__ = "connected_platforms"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    platform = Column(String, nullable=False)  # e.g., telegram, whatsapp
    access_token = Column(String, nullable=False)
    connected_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="platforms")

    preferred_language = Column(String(10), default="en")



# ==================== API KEY MODEL ====================
class APIKey(Base):  # pylint: disable=R0903
    """Stores generated API keys for system integrations."""
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    key = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())



# ==================== SOCIAL MEDIA POST MODEL ====================
class SocialMediaPost(Base):  # pylint: disable=R0903
    """User-generated post content (blog, update, etc.)."""
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="posts")


# ==================== SETTINGS MODEL ====================
class Setting(Base):  # pylint: disable=R0903
    """App-wide configurations stored in key-value format."""
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    value = Column(String(100), nullable=False)


# ==================== PASSWORD RESET MODEL ====================
class PasswordResetCode(Base):  # pylint: disable=R0903
    """Stores verification codes for password reset operations."""
    __tablename__ = "password_reset_codes"

    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String, index=True)
    code = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime)


# ==================== PAYMENT MODEL ====================
class Payment(Base):
    """Records of user payments for subscriptions or services."""
    __tablename__ = "payments"

    id = Column(
        String,
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4())
    )
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    method = Column(String, default="mpesa")
    amount = Column(Float, nullable=False)
    status = Column(String, default="pending")
    phone_number = Column(String, nullable=False)
    reference = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("User", back_populates="payments")


# ==================== SUBSCRIPTION PLANS ====================
class SubscriptionPlan(Base):  # pylint: disable=R0903
    """All subscription packages (e.g. Free, Pro, Business)."""
    __tablename__ = "subscription_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    price = Column(Float, nullable=False, default=0.0)
    duration_days = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)


class UserSubscription(Base):  # pylint: disable=R0903
    """Subscription history and linkage per user."""
    __tablename__ = "user_subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    plan_id = Column(Integer, ForeignKey("subscription_plans.id"), nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="subscriptions")
    plan = relationship("SubscriptionPlan")


# ==================== MESSAGE MODELS ====================
class MessageLog(Base):  # pylint: disable=too-few-public-methods
    """Stores incoming messages from Telegram for admin review and analytics."""
    
    __tablename__ = "message_logs"
    __table_args__ = {'extend_existing': True}  # ✅ epuka conflict kama table ilikuwepo

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(String, index=True, nullable=False)
    sender = Column(String, default="user")
    username = Column(String, nullable=True)
    message = Column(Text, nullable=False)
    received_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<MessageLog(chat_id={self.chat_id}, message={self.message})>"
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)
    vendor_id = Column(Integer, ForeignKey("users.id"))  # 🔁 Link to User
    created_at = Column(DateTime, default=datetime.utcnow)

    vendor = relationship("User", back_populates="products")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

class ScheduledMessage(Base):
    __tablename__ = "scheduled_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(Text, nullable=False)
    platform = Column(String, nullable=False)  # telegram, whatsapp, sms
    recipient = Column(String, nullable=False)  # phone or chat_id
    scheduled_time = Column(DateTime, nullable=False)
    sent = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="scheduled_messages")

    # ================================
# SETTINGS MODEL
# ================================
class Settings(Base):
    __tablename__ = "settings"
    __table_args__ = {'extend_existing': True}  # <-- Hii ndiyo magic line

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    business_name = Column(String, nullable=False)
    tagline = Column(String, nullable=True)
    language = Column(String, nullable=False, default="en")
    logo_url = Column(String, nullable=True)
    primary_color = Column(String, default="#0d6efd")
    secondary_color = Column(String, default="#6c757d")
    timezone = Column(String, default="Africa/Dar_es_Salaam")
    currency = Column(String, default="TZS")
    enable_custom_domain = Column(Boolean, default=False)

    user = relationship("User", back_populates="settings")

class CampaignAffiliate(Base):
    __tablename__ = "campaign_affiliates"
    __table_args__ = (UniqueConstraint('campaign_id', 'user_id', name='uq_campaign_user'),)

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    joined_at = Column(DateTime, default=datetime.utcnow)

    campaign = relationship("Campaign", back_populates="affiliates")
    user = relationship("User", back_populates="joined_campaigns")


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    product_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)

    affiliates = relationship("CampaignAffiliate", back_populates="campaign", cascade="all, delete-orphan")

class ReferralLog(Base):
    __tablename__ = "referral_logs"

    id = Column(Integer, primary_key=True, index=True)
    promoter_id = Column(Integer, ForeignKey("users.id"))
    product_name = Column(String, nullable=False)
    buyer_name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="pending")  # pending, paid
    created_at = Column(DateTime, default=datetime.utcnow)
    promoter = relationship("User", back_populates="referrals")


class LiveSession(Base):
    __tablename__ = "live_sessions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String)
    selected_products = Column(ARRAY(Integer))  # PostgreSQL-specific
    user_id = Column(Integer, ForeignKey("users.id"))
    started_at = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)

    user = relationship("User", back_populates="live_sessions")

class AIBotSettings(Base):
    __tablename__ = "ai_bot_settings"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    active = Column(Boolean, default=True)
    language = Column(String, default="en")
    default_greeting = Column(String, default="Hello! How can I assist you today?")
    platforms = Column(JSON, default=list)

    user = relationship("User", back_populates="ai_bot_settings")

class SupportTicket(Base):
    __tablename__ = "support_tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    subject = Column(String, nullable=False)
    type = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    attachment = Column(String, nullable=True)
    status = Column(String, default="open")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="support_tickets")

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String, nullable=False)
    ip_address = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="audit_logs")

class DroneMission(Base):
    __tablename__ = "drone_missions"

    id = Column(Integer, primary_key=True, index=True)
    drone_id = Column(String)
    product_id = Column(Integer, ForeignKey("products.id"))
    destination = Column(String)
    status = Column(String, default="pending")  # in-transit, delivered, failed
    eta = Column(DateTime)
    initiated_by = Column(String, default="system")  # system/manual/user
    auto_mode = Column(Boolean, default=True)
    emergency = Column(Boolean, default=False)
    retry_attempts = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product")

