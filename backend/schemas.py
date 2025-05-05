"""
Pydantic schemas for SmartBiz Assistant.
Includes user registration, login, tokens, subscriptions, posts, payments, API key management, and broadcasting.
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr, Field, model_validator
from pydantic import BaseModel, HttpUrl
from typing import Optional

# ==================== USER SCHEMAS ====================

class UserBase(BaseModel):
    """Base schema containing shared user fields."""
    username: str
    email: EmailStr
    phone_number: Optional[str] = None
    full_name: Optional[str] = "N/A"
    telegram_id: Optional[int] = None
    business_name: Optional[str] = "N/A"
    business_type: Optional[str] = None
    language: Optional[str] = "sw"
    user_token: Optional[str] = None
    subscription_status: Optional[str] = "free"
    subscription_expiry: Optional[datetime] = None

class UserCreate(UserBase):
    """Input schema for registering a new user."""
    password: str

class User(UserBase):
    """Full user output schema including ID and creation time."""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    """Schema for updating user profile."""
    full_name: Optional[str] = None
    business_name: Optional[str] = None
    business_type: Optional[str] = None
    language: Optional[str] = None
    telegram_id: Optional[int] = None

# ==================== TOKEN SCHEMAS ====================

class Token(BaseModel):
    """Schema for returning access token."""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """Schema representing JWT payload."""
    email: Optional[str] = None

# ==================== LOGIN SCHEMA ====================

class LoginRequest(BaseModel):
    """Schema for login via email, username, or phone."""
    identifier: str
    password: str
    country_code: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def check_country_code_if_phone(cls, values):
        """Check and validate country code format."""
        identifier = values.get("identifier")
        code = values.get("country_code")
        if identifier and (identifier.startswith("0") or identifier.isdigit()):
            if not code:
                raise ValueError("📛 Country code is required for phone login.")
            if not code.startswith("+") or len(code) < 2:
                raise ValueError("📛 Invalid country code format (e.g., +255).")
        return values

# ==================== API KEY SCHEMAS ====================

class APIKeyBase(BaseModel):
    """Base schema for API key operations."""
    name: str

class APIKeyCreate(APIKeyBase):
    """Input schema for creating a new API key."""
    pass

class APIKeyOut(APIKeyBase):
    """Output schema for displaying generated API key."""
    id: int
    key: str
    created_at: datetime

    class Config:
        from_attributes = True

# ==================== SOCIAL MEDIA POST SCHEMAS ====================

class PostBase(BaseModel):
    """Base schema for social media posts."""
    title: str
    content: str

class PostCreate(PostBase):
    """Schema for creating new post."""
    pass

class PostOut(PostBase):
    """Schema for returning post data."""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# ==================== SETTINGS SCHEMAS ====================

class SettingBase(BaseModel):
    """Base schema for application settings."""
    name: str
    value: str

class SettingCreate(SettingBase):
    """Input schema for creating a setting."""
    pass

class SettingOut(SettingBase):
    """Output schema for a setting."""
    id: int

    class Config:
        from_attributes = True

# ==================== FORGOT PASSWORD FLOW ====================

class ForgotPasswordRequest(BaseModel):
    """Schema for requesting a password reset."""
    identifier: str = Field(..., example="juza@example.com or +255712345678")

class VerifyResetCode(BaseModel):
    """Schema for verifying password reset code."""
    identifier: str
    code: str

class ResetPassword(BaseModel):
    """Schema for resetting password using verification code."""
    identifier: str
    code: str
    new_password: constr(min_length=6)

# ==================== SUBSCRIPTION PLAN SCHEMAS ====================

class PlanCreate(BaseModel):
    """Schema for creating a subscription plan."""
    name: str
    price: float
    duration_days: int
    description: Optional[str] = None

class PlanOut(PlanCreate):
    """Schema for viewing a subscription plan."""
    id: int

    class Config:
        from_attributes = True

class SubscribeRequest(BaseModel):
    """Schema for subscribing to a plan."""
    plan_id: int

class SubscriptionOut(BaseModel):
    """Schema for subscription status and dates."""
    user_id: int
    plan_id: int
    start_date: datetime
    end_date: datetime
    is_active: bool

    class Config:
        from_attributes = True

# ==================== PAYMENT SCHEMAS ====================

class PaymentRequest(BaseModel):
    """Schema to initiate a manual payment (e.g., M-PESA)."""
    amount: float
    phone_number: str
    reference: Optional[str] = None

class PaymentResponse(BaseModel):
    """Schema returned after recording payment."""
    id: str
    reference: str
    amount: float
    status: str
    phone_number: str
    method: str
    created_at: datetime
    instructions: str

class ConfirmMpesaRequest(BaseModel):
    """Schema for confirming M-PESA payment manually."""
    reference: str

# ==================== BROADCAST SCHEMA ====================

class BroadcastMessage(BaseModel):
    """Schema for sending bulk messages."""
    message: str
    channels: List[str]  # Example: ["whatsapp", "telegram", "sms"]

# ==================== PRODUCT SCHEMA ====================

class ProductOut(BaseModel):
    """Schema for displaying product information."""
    id: int
    name: str
    description: str
    price: float
    is_available: bool
    created_at: datetime

    class Config:
        from_attributes = True

# ==================== NEGOTIATION SCHEMA ====================

class NegotiationRequest(BaseModel):
    product_id: int
    user_message: str

class NegotiationResponse(BaseModel):
    product_name: str
    original_price: float
    proposed_reply: str
    suggested_discount: Optional[float] = None

# ==================== ADMIN / OWNER SCHEMAS ====================

class RoleUpdateRequest(BaseModel):
    user_id: int
    new_role: str  # 'admin' or 'user'

class AdminCreate(BaseModel):
    email: str
    password: str
    name: str

class OwnerLoginRequest(BaseModel):
    email: EmailStr

class OwnerLoginVerify(BaseModel):
    token: str

# ==================== SMART ORDER SCHEMAS ====================

class SmartOrderOut(BaseModel):
    id: int
    customer_name: str
    product_id: int
    method: str
    created_at: datetime
    status: str

    class Config:
        from_attributes = True

# ==================== PLATFORM CONNECTION SCHEMAS ====================

class PlatformConnectRequest(BaseModel):
    platform: str
    access_token: str

class PlatformOut(BaseModel):
    id: int
    platform: str
    connected_at: datetime

    class Config:
        from_attributes = True

class LanguagePreferenceUpdate(BaseModel):
    language: str

# ==================== CAMPAIGN SCHEDULE SCHEMA ====================

class CampaignRequest(BaseModel):
    product_id: int
    platforms: List[str]
    media_type: Optional[str] = "text"  # "text", "image", "video"
    schedule_time: Optional[datetime]

# ==================== SCHEDULED MESSAGES SCHEMA ====================

class ScheduledMessageCreate(BaseModel):
    message: str
    platform: str
    recipient: str
    scheduled_time: datetime

class ScheduledMessageOut(BaseModel):
    id: int
    message: str
    platform: str
    recipient: str
    scheduled_time: datetime
    sent: bool
    created_at: datetime

    class Config:
        from_attributes = True


# ========== SETTINGS SCHEMAS ==========

class SettingsBase(BaseModel):
    business_name: str
    tagline: Optional[str] = None
    language: Optional[str] = "en"
    logo_url: Optional[HttpUrl] = None
    primary_color: Optional[str] = "#0d6efd"
    secondary_color: Optional[str] = "#6c757d"
    timezone: Optional[str] = "Africa/Dar_es_Salaam"
    currency: Optional[str] = "TZS"
    enable_custom_domain: Optional[bool] = False


class SettingsCreate(SettingsBase):
    pass


class SettingsOut(SettingsBase):
    user_id: str

    class Config:
        from_attributes = True

class AIBotSettingsSchema(BaseModel):
    active: bool = True
    language: str = "en"
    default_greeting: str = "Hello! How can I assist you today?"
    platforms: List[str] = ["whatsapp", "telegram"]

    class Config:
        from_attributes = True

class SupportTicketOut(BaseModel):
    id: int
    user_id: int
    subject: str
    type: str
    description: str
    attachment: Optional[str] = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class AuditLogOut(BaseModel):
    id: int
    user_id: int
    action: str
    target: str
    timestamp: datetime

    class Config:
        from_attributes = True

class SchedulePostSchema(BaseModel):
    platform: str
    content: str
    media_url: Optional[str]
    scheduled_time: datetime
