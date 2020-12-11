import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from config import Config
from src.api import investments, properties


def create_app(_config: Config):
    _app = FastAPI()

    @_app.get("/")
    def index():
        return {"message": "Welcome to properties API"}

    _app.include_router(
        investments.router,
        prefix=f"{_config.API_URL}/investments"
    )

    _app.include_router(
        properties.router,
        prefix=f"{_config.API_URL}/properties"
    )

    register_tortoise(
        _app,
        db_url=_config.DATABASE_URI,
        modules={"models": ["src.models.models"]},
        generate_schemas=True,
        add_exception_handlers=True
    )

    return _app


config = Config.load_config()
app = create_app(config)

if __name__ == '__main__':
    uvicorn.run("main:app", port=config.PORT, reload=True)
