from enum import unique
from tokenize import String

from sqlalchemy import Float
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column


class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = 'user'
    id:Mapped[int]=mapped_column(primary_key=True)
    email:Mapped[str]=mapped_column(String, unique=True)
    password:Mapped[str]=mapped_column(String)

class Trip(Base):
    __tablename__ = 'user'
    id:Mapped[int]=mapped_column(primary_key=True)
    from_city:Mapped[str]=mapped_column(String)
    to_city:Mapped[str]=mapped_column(String)
    price:Mapped[float]=mapped_column(Float)


class Booking(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    : Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)

