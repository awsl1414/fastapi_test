from tortoise import models, fields


class Movie(models.Model):
    name = fields.CharField(max_length=50, null=False, description="电影名称")
    year = fields.CharField(max_length=50, null=False, description="电影年份")
    nickname = fields.CharField(
        max_length=20, null=True, description="昵称", default="你好")
