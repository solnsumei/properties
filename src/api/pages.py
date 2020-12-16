from .baserouter import BaseRouter
from src.models.models import Page, PagePydantic
from src.models.schema.schema import PageSchema

router = BaseRouter(
    response_schema=PagePydantic,
    request_schema=PageSchema,
    model=Page
)
