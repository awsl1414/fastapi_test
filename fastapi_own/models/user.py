from tortoise import models, fields, BaseDBAsyncClient, Iterable
from typing import Any, Coroutine
from core import get_password_hash


class User(models.Model):
    """用户模型

    :param models: _description_
    """

    username = fields.CharField(
        max_length=20, null=False, unique=True, description="账号"
    )
    password = fields.CharField(max_length=128, null=False, description="密码")

    async def save(
        self,
        using_db: BaseDBAsyncClient | None = None,
        update_fields: Iterable[str] | None = None,
        force_create: bool = False,
        force_update: bool = False,
    ) -> Coroutine[Any, Any, None]:
        if force_create or "password" in update_fields:
            self.password = get_password_hash(self.password)
        return await super().save(using_db, update_fields, force_create, force_update)
