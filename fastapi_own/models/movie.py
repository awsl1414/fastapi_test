from tortoise import fields, models


class Movie(models.Model):
    """电影模型

    :param models: _description_
    """

    name = fields.CharField(max_length=50, null=False, description="电影名称")
    year = fields.CharField(max_length=50, null=False, description="电影年份")
