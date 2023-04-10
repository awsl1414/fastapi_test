
from fastapi import APIRouter
from .endpoints import user, movie, login

v1 = APIRouter(prefix="/v1")

v1.include_router(user)
v1.include_router(movie)
v1.include_router(login)
