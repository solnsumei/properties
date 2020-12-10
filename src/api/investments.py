from fastapi import APIRouter
from src.models.models import Investment, InvestmentPydantic
from src.models.schema.schema import InvestmentSchema

router = APIRouter()


@router.get("/")
async def fetch_all():
    return await InvestmentPydantic.from_queryset(Investment.all())


@router.get("/{investment_id}")
async def fetch_investment(investment_id: int):
    return await InvestmentPydantic\
        .from_queryset_single(Investment.get(id=investment_id))


@router.post("/", status_code=201)
async def create(investment: InvestmentSchema):
    new_investment = await Investment.create(
        **investment.dict(), slug=Investment.make_slug(investment.name)
    )
    return await InvestmentPydantic.from_tortoise_orm(new_investment)