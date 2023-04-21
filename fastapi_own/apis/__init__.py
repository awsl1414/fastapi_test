from fastapi import FastAPI

from .login import login
from .user import user
from .movie import movie
from core import config


app = FastAPI(title=config.settings.TITLE, description=config.settings.DESC)

app.include_router(login)
app.include_router(user)
app.include_router(movie)
