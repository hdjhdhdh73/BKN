

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate, UserLogin
from database import get_db
from services.user_services import UserServices

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(data:UserCreate,db:AsyncSession = Depends(get_db)):
    return await UserServices.create_user(db, data.email, data.password)

@router.post("/login")
async def login(data:UserLogin,db:AsyncSession = Depends(get_db)):
    user = await UserServices.login(db, data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="incorect email or password")
    return {"message":"login success","user_id":user.id}
