from pydantic.v1 import BaseModel


class TripCreate(BaseModel):
    from_ciy:str
    to_city:str
    price:float