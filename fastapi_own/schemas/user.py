from tortoise.contrib.pydantic import pydantic_model_creator
import models

User_Pydantic = pydantic_model_creator(models.User, name="User")
UserIn_Pydantic = pydantic_model_creator(
    models.User, name="UserIn", exclude_readonly=True
)
