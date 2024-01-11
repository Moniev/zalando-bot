from app.settings import DATABASE_URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool

class Base(DeclarativeBase):
    pass

'''REQUESTS FOR A CONNECTION TO DATABASE'''
def makeAsyncConnection() -> AsyncEngine | None:
    try: 
        db = create_async_engine(
            url=DATABASE_URL,
            echo=True,
            poolclass=NullPool
        )
        return db
    except:
        return 

connection: AsyncEngine = makeAsyncConnection()

'''ASYNC POSTGRES SESSION OBJECT'''
def asyncSessionLoader() -> async_sessionmaker[AsyncSession]:
    session: AsyncSession = async_sessionmaker(
        bind=connection,
        expire_on_commit=False
    )
    return session

'''ASYNC POSTGRES INITIALIZATION'''
async def createDatabase() -> None:
    connection: AsyncEngine = makeAsyncConnection()
    async with connection.begin() as _connection:
        from app.models import Cart, CreditCard, Item, Login, Logout, Operation, OpenDrop, UpcomingDrop, User
        await _connection.run_sync(Base.metadata.drop_all)
        await _connection.run_sync(Base.metadata.create_all)
    await connection.dispose()
