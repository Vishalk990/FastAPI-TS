from DTO.api import SignUpUser,LoginUser,Token
from fastapi import APIRouter,status,HTTPException,Depends
from helpers import users
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from models.conn_db import Session
from utils.encryption import hash_password,verify_password,create_access_token,oauth2_scheme,get_current_user

router = APIRouter(prefix="/auth",tags=["auth"])

@router.post("/sign-up", status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpUser):
    
    username,email,full_name,password = user.username,user.email, user.full_name, user.password
    user = users.get({"username": username,"email":email})
    
    if user is not None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user already exists")
    
    hashed_password = hash_password(password)
    users.create(
        username=username,
        email=email,
        full_name=full_name,
        password=hashed_password
    )
    
    return {"message": "Sign Up successful"}

        
@router.post("/login")
async def login(request: LoginUser):
    email,password = request.email, request.password
    user = users.get({"email": email})
    
    if user:
        hashed_password = user.password
        if verify_password(password,hashed_password):
            token = create_access_token(user)
            return {"message": "Login successful","jwt": token}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="password incorrect")
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="email invalid")

@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get({"username": form_data.username})
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid user")
    
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    access_token = create_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}