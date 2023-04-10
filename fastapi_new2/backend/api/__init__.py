"""
create app
"""

import sys
import logging
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from .login import login
from .movie import movie
from .user import user


app = FastAPI()

app.include_router(user, prefix="/user")
app.include_router(login, prefix="/login")
app.include_router(movie, prefix="/movie")

fmt = logging.Formatter(
    fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)
sh.setFormatter(fmt)

# will print debug sql
logger_db_client = logging.getLogger("tortoise.db_client")
logger_db_client.setLevel(logging.DEBUG)
logger_db_client.addHandler(sh)

logger_tortoise = logging.getLogger("tortoise")
logger_tortoise.setLevel(logging.DEBUG)
logger_tortoise.addHandler(sh)

register_tortoise(
    app,
    db_url="sqlite://watch.sqlite",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)