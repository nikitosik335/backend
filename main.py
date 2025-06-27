from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import requests as rq
from pydantic import BaseModel

class NewUser(BaseModel):
    name:str
    password:str

@asynccontextmanager
async def lifespan(app:FastAPI):
    await rq.init_db()
    print('bot is ready')
    yield
    print('bot was deactivated')

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_headers = ['*'],
    allow_credentials = ['*'],
    allow_methods = ['*'],
)

@app.get('/profile')
async def profile(name:str,password:str):
    user = await rq.get_user(name)
    if not user:
        return {'status':'not definded'}
    elif user.password == password:
        return user
    else:
        return {'status':'password is invalid'}

@app.post('/add_user')
async def add_user(newUser: NewUser):
    await rq.add_user(newUser.name,newUser.password)
    return {'status':'ok'}