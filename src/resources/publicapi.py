from .baserouter import APIRouter
from src.models.models import Investment, InvestmentPydantic,\
    Property, PropertyPydantic, Page, PagePydantic


router = APIRouter()


@router.get('/investments', response_model=list[InvestmentPydantic])
async def get_all_investments():
    return await InvestmentPydantic.from_queryset(Investment.all())


@router.get('/investments/{slug}', response_model=InvestmentPydantic)
async def get_investment(slug: str):
    return await InvestmentPydantic.from_queryset_single(Investment.get(slug=slug))


@router.get('/properties', response_model=list[PropertyPydantic])
async def get_all_properties():
    return await PropertyPydantic.from_queryset(Property.all())


@router.get('/properties/{slug}', response_model=PropertyPydantic)
async def get_property(slug: str):
    return await PropertyPydantic.from_queryset_single(Property.get(slug=slug))


@router.get('/pages/{slug}', response_model=PagePydantic)
async def get_page(slug: str):
    return await PagePydantic.from_queryset_single(Page.get(slug=slug))
