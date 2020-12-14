from tortoise.contrib.fastapi import register_tortoise


def init_db(_config, _app):
    register_tortoise(
        _app,
        db_url=_config.DATABASE_URI,
        modules={"models": ["src.models.models"]},
        generate_schemas=True,
        add_exception_handlers=True
    )
