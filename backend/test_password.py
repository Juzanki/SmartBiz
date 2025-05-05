from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Tumia hash yako halisi hapa chini 👇
password = "$2b$12$aYUkhpN0pCOOfQc8lCVDPOrJ5iIdBkWWSGirDGPhvtSqrOgWfQWBm"
plain_password = "testingpass123"

is_valid = pwd_context.verify(plain_password, hashed_password)

print("✅ Match!" if is_valid else "❌ Invalid password")
