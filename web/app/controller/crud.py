from app import asyncSessionLoader
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.sql.selectable import Select


class CRUD():
    def __init__(self, id: int):
        self.__id: int = id

    @property
    def id(self):
        return self.__id

    async def getAll(self, item: object, async_session: async_sessionmaker[AsyncSession]=asyncSessionLoader()) -> list[object] | None:
        async with async_session() as session: 
            statement: Select = select(item).order_by(item.id)
            result = await session.execute(statement=statement)
            await session.close()
            return result.scalars()

    async def getItemById(self, item: object, id: int, async_session: async_sessionmaker[AsyncSession]=asyncSessionLoader()) -> object | None:
        async with async_session() as session:
            statement: Select = select(item).filter(item.id == id)
            result = await session.execute(statement=statement)
            await session.close()
            return result.scalars()

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
        

