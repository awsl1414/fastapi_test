from tortoise.contrib.fastapi import register_tortoise
from uvicorn import run
from apis import app

register_tortoise(
    app,
    db_url="sqlite://watch.sqlite",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    run(app="main:app", reload=True)
