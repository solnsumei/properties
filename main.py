import uvicorn
from fastapi import FastAPI, Depends
from config import Config
from db import init_db
from src.api import investments, properties, auth
from src.utils import security


def create_app(_config: Config):
    _app = FastAPI()

    @_app.get("/")
    def index():
        return {"message": "Welcome to properties API"}

    _app.include_router(
        auth.router,
        prefix=f"{_config.API_URL}/auth",
        tags=["Authentication"]
    )

    _app.include_router(
        investments.router,
        prefix=f"{_config.API_URL}/investments",
        dependencies=[Depends(security.get_current_user)],
        tags=["Investments"]
    )

    _app.include_router(
        properties.router,
        prefix=f"{_config.API_URL}/properties",
        dependencies=[Depends(security.get_current_user)],
        tags=["Properties"]
    )

    return _app


# Load configuration
config = Config.load_config()

# Create app
app = create_app(config)

# Initialize database
init_db(_config=config, _app=app)

if __name__ == '__main__':
    uvicorn.run("main:app", port=config.PORT, reload=True)
