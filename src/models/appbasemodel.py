from pydantic import BaseModel
from tortoise import fields, models


class AppBaseModel(models.Model):
    id = fields.IntField(pk=True)

    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)

    """ Database methods """

    @classmethod
    async def find_all(cls):
        return await cls.all()

    @classmethod
    async def find_by(cls, **kwargs):
        return await cls.filter(**kwargs).all()

    @classmethod
    async def find_one(cls, **kwargs):
        return await cls.filter(**kwargs).first()

    @classmethod
    async def find_by_id(cls, _id: int):
        return await cls.get(id=_id)

    @classmethod
    async def create_one(cls, item: BaseModel):
        return await cls.create(**item.dict())

    @classmethod
    async def update_one(cls, _id: int, item: BaseModel):
        await cls.filter(_id=id).update(**item.dict(exclude_unset=True))
        return await cls.find_by_id(_id)

    @classmethod
    async def delete_one(cls, _id: int) -> int:
        deleted_count = await cls.filter(_id=id).delete()
        return deleted_count

    class Meta:
        __abstract__ = True
