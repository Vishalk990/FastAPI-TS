from passlib.context import CryptContext
from models.models import Users
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta,datetime
from pytz import timezone
from typing import Annotated
import os
import jwt

SECRET_KEY = os.environ.get("JWT_SECRET")
ALGORITHM = os.environ.get("ALGORITHM")
JWT_TOKEN_EXPIRY_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

bcrypt = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str) -> str:
    return bcrypt.hash(password)

def verify_password(password:str,hashed_password:str) -> bool:
    return bcrypt.verify(password,hashed_password)

def create_access_token(user: Users):
    data = {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "exp": datetime.now(timezone("Asia/Kolkata")) + timedelta(minutes=int(JWT_TOKEN_EXPIRY_MINUTES)),
    }
   
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    
def get_current_user(token: Annotated[str,Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise HTTPException(status_code=401,detail="invalid token")
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401,detail="token expired")
    
