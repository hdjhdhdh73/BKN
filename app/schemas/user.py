from pydantic import BaseModel


class UserCreate(BaseModel):
    email:str
    password:str
    fullname:str | None=None
    phone: str | None = None
    role:str="user"

class UserLogin(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    email:str | None=None
    password:str | None=None
    fullname: str | None = None
    phone: str | None = None
