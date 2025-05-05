from jose import jwt

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# Hakikisha hii token ni kamili kabisa
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaXpvd25lckBleGFtcGxlLmNvbSIsImV4cCI6MTcxMjMzNzU1OH0.5ZKdcOg5J6KXzAaeHfPy-xjFZZx3Aex1n6GHLOJCyqI"

decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print("Decoded token:", decoded)
