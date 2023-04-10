
import sys
import logging
from tortoise.contrib.fastapi import register_tortoise
from scheams import Movie_Pydantic, MovieIn_Pydantic
from models import Movie
from typing import List
from fastapi import FastAPI
from uvicorn import run


"""
登录、注册
"""

app = FastAPI()


@app.post("/login", summary="登录")
async def user_login():
    pass


@app.get("/movie", summary="电影列表", response_model=List[Movie_Pydantic])
async def movie_list():
    return await Movie_Pydantic.from_queryset(Movie.all())


@app.post("/movie", summary="新增电影", response_model=MovieIn_Pydantic)
async def movie_create(movie_form: MovieIn_Pydantic):
    return await Movie_Pydantic.from_orm(Movie.create(**movie_form.dict()))
    pass


@app.put("/movie", summary="编辑电影")
async def movie_update():
    pass


@app.delete("/movie", summary="删除电影")
async def movie_delete():
    pass

'USER'


@app.get("/user", summary="当前用户")
async def user_info():
    pass


@app.put("/user", summary="修改信息")
async def user_update():
    pass

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


if __name__ == '__main__':
    run("main:app", reload=True)
