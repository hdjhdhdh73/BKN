from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.schemas.booking import BookingCreate
from database import get_db
from services.booking_services import BookingServices

router = APIRouter(prefix="/bookings",tags=["Bookings"])

@router.post("/")
async def create_booking(data:BookingCreate,db:AsyncSession=Depends(get_db)):
    return await BookingServices.create_booking(db, data)

@router.get("/")
async def get_booking(db:AsyncSession=Depends(get_db)):
    return await BookingServices.get_all(db)
