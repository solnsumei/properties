import uvicorn
from fastapi import FastAPI
from config import Config


def create_app(_config: Config):
    _app = FastAPI()

    @_app.get("/")
    def index():
        return {"message": "Welcome to properties API"}

    return _app


config = Config.load_config()
app = create_app(config)

if __name__ == '__main__':
    uvicorn.run("main:app", port=config.PORT, reload=True)
