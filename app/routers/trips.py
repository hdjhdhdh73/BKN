

from fastapi import APIRouter, HTTPException
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
async def get_trip(from_city:str | None=None,
                   to_city:str  | None=None,
                   db:AsyncSession=Depends(get_db)):
    return await TripServices.get_all(db,from_city,to_city)

@router.get("/{trip_id}")
async def get_trips(trip_id:int,db:AsyncSession=Depends(get_db)):
    trip = await TripServices.get_by_id(db,trip_id)
    if not trip:
        return HTTPException(status_code=404)
    return trip