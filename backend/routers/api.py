from fastapi import APIRouter,Depends
from utils.encryption import get_current_user

router = APIRouter(prefix="/dashboard",tags=["dashboard"])

@router.get("/home")
async def home_page(current_user: str = Depends(get_current_user)):
    return {"message": "Homepage","current_user": current_user}