from DTO.api import User
from fastapi import APIRouter,status,HTTPException
from helpers import users

router = APIRouter(prefix="/auth",tags=["auth"])

@router.post("/sign-up", status_code=status.HTTP_201_CREATED)
async def signup(user: User):
    username,email,full_name = user.username,user.email, user.full_name
    user = users.get({"username": username,"email":email})
    
    if user is not None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user already exists")
    
    users.create(
        username=username,
        email=email,
        full_name=full_name
    )
    
    return {"message": "Sign up successful"}
    
    
    
    
# @router.post("login")
# async def login(user:User)
    