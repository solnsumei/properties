from src.models.models import Investment, InvestmentPydantic
from src.models.schema.schema import InvestmentSchema
from .baserouter import BaseRouter

router = BaseRouter(
    request_schema=InvestmentSchema,
    response_schema=InvestmentPydantic,
    model=Investment
)

router.load_crud_routes()
