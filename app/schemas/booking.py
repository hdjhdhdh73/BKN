from pydantic.v1 import BaseModel


class BookingCreate(BaseModel):
    user_id:int
    trip_id:int
