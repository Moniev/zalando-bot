from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app import Base

class Cart(Base):
    id: Mapped[int] = mapped_column()

    def __init__(self, id: int):
        self.id: int = id

    def __repr__(self):
        return 

class Item(Base):
    id: Mapped[int] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey())
    cart_id: Mapped[int] = mapped_column(ForeignKey())
    bought: Mapped = mapped_column()
    shipped: Mapped = mapped_column()

    def __init__(self, id: int, bought: datetime, shipped: datetime):
        self.id: int = id
        self.bought: datetime = bought
        self.shipped: datetime = shipped 

    def __repr__(self):
        return 

class User(Base):
    id: Mapped[int] = mapped_column()
    nickname: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    registration: Mapped[datetime] = mapped_column()
    activated: Mapped[bool] = mapped_column()
    items: Mapped['Item'] = relationship() 

    def __init__(self, id: int, nickname: str, password: str, email: str, registration: datetime, activated: bool):
        self.id: int = id
        self.nickname: str = nickname
        self.password: str = password
        self.email: str = email
        self.registration: datetime = registration
        self.activated: bool = activated

    def __repr__(self):
        return 
    

class CreditCard(Base):
    id: Mapped[int] = mapped_column()
    credit_card_id: Mapped[str] = mapped_column()