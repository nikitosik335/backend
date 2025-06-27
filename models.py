from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(DeclarativeBase, AsyncAttrs):
    pass

class User(Base):
    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(20))
    password:Mapped[str] = mapped_column(String(30))