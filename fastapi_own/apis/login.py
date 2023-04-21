from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

import models
from core import verify_password, create_access_token

login = APIRouter(tags=["登录相关"])


@login.post("/login", summary="登录")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    if user := await models.User.get(username=form_data.username):
        if verify_password(form_data.password, user.password):
            token = create_access_token({"sub": user.username})
            return {
                "access_token": token,
                "token_type": "bearer",
            }
    return {"msg": "账号或密码错误"}


@login.put("/logout", summary="注销")
async def user_login():
    pass
