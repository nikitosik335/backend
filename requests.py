from models import Base, User
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import select

engine = create_async_engine('sqlite+aiosqlite:///db.sqlite3',echo = True)
async_session = async_sessionmaker(bind = engine,expire_on_commit=True)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_user(name:str) -> User:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.name == name))
        if user:
            return user

async def add_user(name:str,password:str) -> None:
    async with async_session() as session:
        new_user = User(name = name, password = password)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user