from fastapi import APIRouter
from typing import List
from schemas import Movie_Pydantic, MovieIn_Pydatic
import models

movie = APIRouter(tags=["电影相关"])


@movie.get("/movie/list", summary="电影列表", response_model=List[Movie_Pydantic])
async def movie_list(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    return await Movie_Pydantic.from_queryset(
        models.Movie.all().offset(skip).limit(limit)
    )


@movie.post("/movie/create", summary="新增电影", response_model=Movie_Pydantic)
async def movie_create(movie_form: MovieIn_Pydatic):
    movie_obj = await models.Movie.create(**movie_form.dict(exclude_unset=True))
    return await Movie_Pydantic.from_tortoise_orm(movie_obj)


@movie.put("/movie/update", summary="更新电影")
async def movie_update(pk: int, movie: MovieIn_Pydatic):
    if await models.Movie.filter(pk=pk).update(**movie.dict(exclude_unset=True)):
        return {"msg": "更新成功"}
    return {"msg": "更新失败"}


@movie.delete("/movie/delete", summary="删除电影")
async def movie_delete(pk: int):
    if await models.Movie.filter(pk=pk).delete():
        return {"msg": "删除成功"}
    return {"msg": "删除失败"}
