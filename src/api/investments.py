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
    new_investment = await Investment.create_one(investment)
    return await InvestmentPydantic.from_tortoise_orm(new_investment)


@router.put("/{investment_id}")
async def update(investment_id: int, investment: InvestmentSchema):
    updated_investment = await Investment.update_one(investment_id, investment)
    return await InvestmentPydantic.from_queryset_single(updated_investment)


@router.delete("/{investment_id}")
async def delete(investment_id: int):
    await Investment.delete_one(investment_id)
    return {"message": "Item deleted successfully"}
