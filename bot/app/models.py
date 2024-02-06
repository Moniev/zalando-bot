from app import Base
from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Cart(Base):
    __bind_key__ = "Cart"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"), nullable=False)
    items: Mapped['Item'] = relationship("Item", backref="Cart", foreign_keys="Item.cart_id")
    __tablename__ = "Cart"

    def __init__(self, user_id: int):
        self.user_id: int = user_id

    def __repr__(self):
        return f"[Cart   ][id: {self.id}][user_id: {self.user_id}]"


class Item(Base):
    __bind_key__ = "Item"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    cart_id: Mapped[int] = mapped_column(Integer, ForeignKey("Cart.id"), nullable=False)
    bought_datetime: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    shipped_datetime: Mapped[DateTime] = mapped_column(Boolean, nullable=False)
    __tablename__ = "Item"

    def __init__(self, bought_datetime: datetime, shipped_datetime: datetime):
        self.bought_datetime: datetime = bought_datetime
        self.shipped_datetime: datetime = shipped_datetime

    def __repr__(self):
        return f"[Item   ][id: {self.id}][cart_id: {self.cart_id}][bought: {self.bought_datetime}][shipped: {self.shipped_datetime}]"


class User(Base):
    __bind_key__ = "User"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    registration_datetime: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    cart: Mapped['Cart'] = relationship("Cart", backref="User", foreign_keys="Cart.user_id") 
    logins: Mapped['Login'] = relationship("Login", backref="User", foreign_keys="Login.user_id")
    logouts: Mapped['Logout'] = relationship("Logout", backref="User", foreign_keys="Logout.user_id")
    website_logins: Mapped['WebsiteLoginInfo'] = relationship("WebsiteLoginInfo", backref="User", foreign_keys="WebsiteLoginInfo.user_id")
    website_logouts: Mapped['WebsiteLogoutInfo'] = relationship("WebsiteLogoutInfo", backref="User", foreign_keys="WebsiteLogoutInfo.user_id")
    __tablename__ = "User"

    def __init__(self, nickname: str, password: str, email: str, registration_datetime: datetime, active: bool):
        self.nickname: str = nickname
        self.password: str = password
        self.email: str = email
        self.registration_datetime: datetime = registration_datetime
        self.active: bool = active

    def __repr__(self):
        return f"[User   ][id: {self.id}][nickname: {self.nickname}][password: {self.password}][email: {self.email}][registration: {self.registration}][active: {self.active}]"
    

class Login(Base):
    __bind_key__ = "Login"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"), nullable=False)
    success: Mapped[bool] = mapped_column(Boolean, nullable=False)
    date_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(), nullable=False)
    __tablename__ = "Login"

    def __init__(self, user_id: int, success: bool, date_time: datetime):
        self.user_id: int = user_id
        self.success: bool = success
        self.date_time:  datetime =  datetime 

    def __repr__(self):
        return f"[Login   ][id: {self.id}][user_id: {self.user_id}][success: {self.success}][date: {self.date}]"


class Logout(Base):
    __bind_key__ = "Logout"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"), nullable=False)
    success: Mapped[bool] = mapped_column(Boolean, nullable=False)
    date_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(), nullable=False)
    __tablename__ = "Logout"

    def __init__(self, user_id: int, success: bool, date_time: datetime):
        self.user_id: int = user_id
        self.success: bool = success
        self.date_time: datetime =  date_time 

    def __repr__(self):
        return f"[Logout   ][id: {self.id}][user_id: {self.user_id}][success: {self.success}][date: {self.date}]"


class UpcomingDrop(Base):
    __bind_key__ = "UpcomingDrop"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    website_id: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[String] = mapped_column(String, nullable=False)
    open_datetime: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    __tablename__ = "UpcomingDrop"

    def __init__(self, website_id: str, title: str, open_datetime: datetime):
        self.website_id: str = website_id
        self.title: str = title 
        self.open_datetime: datetime = open_datetime

    def __repr__(self):
        return f"[UpcomingDrop   ][id: {self.id}][title: {self.title}][drop_date: {self.open_datetime}]"


class OpenDrop(Base):
    __bind_key__ = "OpenDrop" 
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    website_id: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[String] = mapped_column(String, nullable=False)
    end_datetime: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    __tablename__ = "OpenDrop"

    def __init__(self, website_id: str, title: str, end_datetime: datetime):
        self.website_id: str = website_id
        self.title: str = title 
        self.end_datetime: datetime = end_datetime

    def __repr__(self):
        return f"[OpenDrop   ][id: {self.id}][title: {self.title}][drop_date: {self.end_datetime}]"


class CreditCard(Base):
    __bind_key__ = "CreditCard"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    credit_card_id: Mapped[str] = mapped_column(String, nullable=False)
    cash_left: Mapped[float] = mapped_column(Float, nullable=False)
    used: Mapped[bool] = mapped_column(Boolean, nullable=False) 
    __tablename__ = "CreditCard"

    def __init__(self, credit_card_id: str, cash_left: float, used: bool):
        self.credit_card_id: str = credit_card_id
        self.cash_left: bool = cash_left
        self.used: bool = used

    def __repr__(self):
        return f"[CreditCard   ][id: {self.id}][credit_cart_id: {self.credit_card_id}][cash_left: {self.cash_left}][used: {self.used}]"
    

class Operation(Base):
    __bind_key__ = "Operation"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"), nullable=False)
    operation_name: Mapped[str] = mapped_column(String, nullable=False)
    success: Mapped[bool] = mapped_column(Boolean, nullable=False)
    __tablename__ = "Operation"

    def __init__(self, user_id: int, operation_name: str, success: bool):
        self.user_id: int = user_id
        self.operation_name: str = operation_name
        self.success: bool = success

    def __repr__(self):
        return f"[Operation   ][id: {self.id}][user_id: {self.user_id}][operation_name: {self.operation_name}][success: {self.success}]"


class WebsiteLoginInfo(Base):
    __bind_key__ = "WebsiteLoginInfo"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"), nullable=False)
    date_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), nullable=False)
    __tablename__ = "WebsiteLoginInfo"

    def __init__(self, user_id: int):
        self.user_id: int = user_id

    def __repr__(self):
        return f"[WebsiteLoginInfo   ][id: {self.id}][user_id: {self.user_id}][date_time: {self.date_time}]"
    

class WebsiteLogoutInfo(Base):
    __bind_key__ = "WebsiteLogoutInfo"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"), nullable=False)
    date_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), nullable=False)
    __tablename__ = "WebsiteLogoutInfo"

    def __init__(self, user_id: int):
        self.user_id: int = user_id

    def __repr__(self):
        return f"[WebsiteLogoutInfo   ][id: {self.id}][user_id: {self.user_id}][date_time: {self.date_time}]"