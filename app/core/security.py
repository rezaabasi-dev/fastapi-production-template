from passlib.context import CryptContext
from jose import jwt

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(data, secret):
    return jwt.encode(data, secret, algorithm="HS256")
