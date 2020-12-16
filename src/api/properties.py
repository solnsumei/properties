from src.models.models import Property, PropertyPydantic
from src.models.schema.schema import PropertySchema
from .baserouter import BaseRouter


router = BaseRouter(
    request_schema=PropertySchema,
    response_schema=PropertyPydantic,
    model=Property
)

router.load_crud_routes()
