from fastapi import Depends
from src.resources import investments, properties, auth, pages, publicapi
from src.utils import security


def add_routers(app, config):
    """
    Include routes
    :param app:
    :param config:
    :return: None
    """
    app.include_router(
        auth.router,
        prefix=f"{config.API_URL}/auth",
        tags=["Authentication"]
    )

    app.include_router(
        investments.router,
        prefix=f"{config.API_URL}/admin/investments",
        dependencies=[Depends(security.get_current_user)],
        tags=["Admin/Investments"]
    )

    app.include_router(
        pages.router,
        prefix=f"{config.API_URL}/admin/pages",
        dependencies=[Depends(security.get_current_user)],
        tags=["Admin/Pages"]
    )

    app.include_router(
        properties.router,
        prefix=f"{config.API_URL}/admin/properties",
        dependencies=[Depends(security.get_current_user)],
        tags=["Admin/Properties"]
    )

    app.include_router(
        publicapi.router,
        prefix=f"{config.API_URL}",
        tags=["PublicApi"]
    )
