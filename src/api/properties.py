from fastapi import APIRouter
from src.models.models import Property, PropertyPydantic
from src.models.schema.schema import PropertySchema

router = APIRouter()


@router.get("/")
async def fetch_all():
    return await PropertyPydantic.from_queryset(Property.all())


@router.get("/{property_id}")
async def fetch_one(property_id: int):
    return await PropertyPydantic\
        .from_queryset_single(Property.get(id=property_id))


@router.post("/", status_code=201)
async def create(item: PropertySchema):
    new_property = await Property.create_one(item)
    return await PropertyPydantic.from_tortoise_orm(new_property)


@router.put("/{property_id}")
async def update(property_id: int, item: PropertySchema):
    updated_property = await Property.update_one(property_id, item)
    return await PropertyPydantic.from_queryset_single(updated_property)


@router.delete("/{property_id}")
async def delete(property_id: int):
    await Property.delete_one(property_id)
    return {"message": "Item deleted successfully"}
