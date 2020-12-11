from src.models.models import Investment, InvestmentPydantic
from src.models.schema.schema import InvestmentSchema
from .baserouter import base_crud_router


router = base_crud_router(
    request_schema=InvestmentSchema,
    response_schema=InvestmentPydantic,
    model=Investment
)
