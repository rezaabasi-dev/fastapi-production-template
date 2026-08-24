from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings

ALGORITHM = "HS256"

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=24)
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=ALGORITHM)
