from app import asyncSessionLoader
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession


class CRUD():
    def __init__(self):
        pass

    async def getAll(self, item: object, async_session: async_sessionmaker[AsyncSession]=asyncSessionLoader()) -> object | None:
        async with async_session() as session: 
            statement = select(item).order_by(item.id)
            result = await session.execute(statement=statement)
            return session.scalars()

    async def add(self, item: object, async_session: async_sessionmaker[AsyncSession]=asyncSessionLoader()) -> object | None:
        async with async_session() as session:   
            session.add(item)   
            await session.commit()
            await session.refresh(item)
            await session.close()
            return item
                        
    async def delete(self, item: object, async_session: async_sessionmaker[AsyncSession]=asyncSessionLoader()) -> object | None:
        async with async_session() as session:
            session.delete(item)
            await session.commit()
            await session.refresh(item)
            await session.close()
            return item
        
    async def getAllItems(self, item: object, async_session: async_sessionmaker[AsyncSession]=asyncSessionLoader()) -> list[object] | list[None]:
        async with async_session() as session:
            pass
