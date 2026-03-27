from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.models.models import User


class UserServices:
    @staticmethod
    async def create_user(db:AsyncSession,data):
        user = User(**data.dict())
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def login(db:AsyncSession, email:str, password:str):
        result = await db.execute(select(User).where(User.email==email))
        user = result.scalar_one_or_none()
        if not user or user.password !=password:
            return None
        return user

    @staticmethod
    async def get_user_by_id(db:AsyncSession,user_id:int):
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_user_all(db:AsyncSession):
        result = await db.execute(select(User))
        return result.scalars().all()

    @staticmethod
    async def update_user(db:AsyncSession,user_id:int,data):
        user = await db.execute(select(User).where(User.id == user_id))
        user = user.scalar_one_or_none()
        if not user:
            return None
        if data.email is not None:
            user.email = data.email
        if data.password is not None:
            user.password =data.password
        if data.fullname is not None:
            user.fullname = data.fullname
        if data.phone is not None:
            user.phone = data.phone
        await db.commit()
        await db.refresh(user)
        return user


    @staticmethod
    async def delete_user(db:AsyncSession,user_id:int):
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            return None
        await db.delete(user)
        await db.commit()
        return user



