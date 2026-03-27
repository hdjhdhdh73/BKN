from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.trip import TripCreate
from database import get_db
from services.trip_services import TripServices

router = APIRouter(prefix="/trip",tags=["Trips"])
@router.post("/")
async def create_trip(data:TripCreate,db:AsyncSession=Depends(get_db)):
    return await TripServices.create_trip(db, data)

@router.get("/")
async def get_trip(db:AsyncSession=Depends(get_db)):
    return await TripServices.get_all(db)
