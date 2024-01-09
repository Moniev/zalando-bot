from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Float, Integer, String, select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

class Cart(Base):
    __bind_key__ = "Cart"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"), nullable=False)
    items: Mapped['Item'] = relationship("Item", backref="Cart", foreign_keys="Item.id")
    __tablename__ = "Cart"

    def __init__(self, id: int, user_id: int):
        self.id: int = id
        self.user_id: int = user_id

    def __repr__(self):
        return f""

class Item(Base):
    __bind_key__ = "Item"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    cart_id: Mapped[int] = mapped_column(Integer, ForeignKey("Cart.id"), nullable=False)
    bought: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    shipped: Mapped[DateTime] = mapped_column(Boolean, nullable=False)
    __tablename__ = "Item"

    def __init__(self, id: int, bought: datetime, shipped: datetime):
        self.id: int = id
        self.bought: datetime = bought
        self.shipped: datetime = shipped 

    def __repr__(self):
        return f""

class User(Base):
    __bind_key__ = "User"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    nickname: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    registration: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    cart: Mapped['Cart'] = relationship("Cart", backref="User", foreign_keys="Cart.user_id") 
    logins: Mapped['Login'] = relationship("Login", backref="User")
    logouts: Mapped['Logout'] = relationship("Logout", backref="User")
    __tablename__ = "User"

    def __init__(self, id: int, nickname: str, password: str, email: str, registration: DateTime, active: bool):
        self.id: int = id
        self.nickname: str = nickname
        self.password: str = password
        self.email: str = email
        self.registration: DateTime = registration
        self.active: bool = active

    def __repr__(self):
        return f""
    
class Login(Base):
    __bind_key__ = "Login"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"), nullable=False)
    success: Mapped[bool] = mapped_column(Boolean, nullable=False)
    date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    __tablename__ = "User"

    def __init__(self, id: int, user_id: int, date: DateTime):
        self.id: int = id
        self.user_id: int = user_id
        self.date: DateTime = date 

    def __repr__(self):
        return f""

class Logout(Base):
    __bind_key__ = "Logout"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"), nullable=False)
    success: Mapped[bool] = mapped_column(Boolean, nullable=False)
    date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    __tablename__ = "Logout"

    def __init__(self, id: int, user_id: int, date: DateTime):
        self.id: int = id
        self.user_id: int = user_id
        self.date: DateTime = date 

    def __repr__(self):
        return

class Drop(Base):
    __bind_key__ = "Drop"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    title: Mapped[String] = mapped_column(String, nullable=False)
    drop_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    __tablename__ = "Drop"

    def __init__(self, id: int, item_id: str, title: str, drop_date: DateTime):
        self.id: int = id
        self.title: str = title 
        self.drop_date: DateTime = drop_date

    def __repr__(self):
        return f"[drop   ][id: {self.id}][title: {self.title}][drop_date: {self.drop_date}]"

class CreditCard(Base):
    __bind_key__ = "CreditCard"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    credit_card_id: Mapped[str] = mapped_column(String, nullable=False)
    cash_left: Mapped[float] = mapped_column(Float, nullable=False)
    used: Mapped[bool] = mapped_column(Boolean, nullable=False) 
    __tablename__ = "CreditCard"

    def __init__(self, id: int, credit_card_id: str, cash_left: float, used: bool):
        self.id: int = id
        self.credit_card_id: str = credit_card_id
        self.cash_left: bool = cash_left
        self.used: bool = used

    def __repr__(self):
        return f"[credit_card   ][id: {self.id}][credit_cart_id: {self.credit_card_id}][cash_left: {self.cash_left}][used: {self.used}]"