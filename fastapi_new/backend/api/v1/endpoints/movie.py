
from fastapi import APIRouter
from typing import List
from models import Movie
from scheams import Movie_Pydantic, MovieIn_Pydantic

movie = APIRouter(tags=["电影相关"])


@movie.get("/movie", summary="电影列表", response_model=List[Movie_Pydantic])
async def movie_list():
    return await Movie_Pydantic.from_queryset(Movie.all())


@movie.post("/movie", summary="新增电影", response_model=MovieIn_Pydantic)
async def movie_create(movie_form: MovieIn_Pydantic):
    return await Movie_Pydantic.from_orm(Movie.create(**movie_form.dict()))
    pass


@movie.put("/movie", summary="编辑电影")
async def movie_update():
    pass


@movie.delete("/movie", summary="删除电影")
async def movie_delete():
    pass
