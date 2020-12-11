from fastapi import APIRouter


def base_crud_router(request_schema, response_schema, model):
    router = APIRouter()

    @router.get("/")
    async def fetch_all():
        return await response_schema.from_queryset(model.all())

    @router.get("/{item_id}")
    async def fetch_one(item_id: int):
        return await response_schema \
            .from_queryset_single(model.get(id=item_id))

    @router.post("/", status_code=201)
    async def create(item: request_schema):
        new_item = await model.create_one(item)
        return await response_schema.from_tortoise_orm(new_item)

    @router.put("/{item_id}")
    async def update(item_id: int, item: request_schema):
        updated_item = await model.update_one(item_id, item)
        return await response_schema.from_queryset_single(updated_item)

    @router.delete("/{item_id}")
    async def delete(item_id: int):
        await model.delete_one(item_id)
        return {"message": "Item deleted successfully"}

    return router
