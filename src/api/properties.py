from src.models.models import Property, PropertyPydantic
from src.models.schema.schema import PropertySchema
from .baserouter import base_crud_router

router = base_crud_router(
    request_schema=PropertySchema,
    response_schema=PropertyPydantic,
    model=Property
)
