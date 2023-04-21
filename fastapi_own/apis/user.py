from fastapi import APIRouter
from schemas import UserIn_Pydantic
import models

user = APIRouter(tags=["用户相关"])


@user.get("/user/list", summary="用户列表")
async def user_list():
    pass


@user.post("/user/create", summary="新增用户")
async def user_create(user: UserIn_Pydantic):
    await models.User.create(**user.dict())
    return {"msg": "新建成功"}


@user.put("/user/update", summary="更新用户")
async def user_update():
    pass


@user.delete("/user/delete", summary="删除用户")
async def user_delete():
    pass
