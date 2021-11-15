from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import User, Gender, Role
app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name='hadi',
        last_name='purnomo',
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name='nana',
        last_name='savitri',
        gender=Gender.female,
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        first_name='eko',
        last_name='asolole',
        gender=Gender.female,
        roles=[Role.student]
    )
]


@app.get('/')
def root():
    return{"hello": "world"}


@app.get('/api/v1/users')
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
