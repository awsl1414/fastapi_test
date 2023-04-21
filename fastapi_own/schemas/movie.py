from tortoise.contrib.pydantic import pydantic_model_creator
import models

Movie_Pydantic = pydantic_model_creator(models.Movie, name="Movie")
MovieIn_Pydatic = pydantic_model_creator(
    models.Movie, name="MovieIn", exclude_readonly=True
)
