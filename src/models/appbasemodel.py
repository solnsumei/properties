from src.utils.status import Status
from slugify import slugify
from tortoise import fields, models


class AppBaseModel(models.Model):
    id = fields.IntField(pk=True)
    status = fields.CharEnumField(Status, default=Status.ACTIVE)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)

    """ Database methods """
    @classmethod
    async def find_by(cls, **kwargs):
        return await cls.filter(**kwargs).all()

    @classmethod
    async def find_one(cls, **kwargs):
        return await cls.filter(**kwargs).first()

    @classmethod
    async def update_one(cls, _id: int, item):
        await cls.filter(id=_id).update(**item.dict(exclude_unset=True))
        return cls.get(id=_id)

    @classmethod
    async def delete_one(cls, _id: int) -> int:
        deleted_count = await cls.filter(id=_id).delete()
        return deleted_count

    """ Utility methods """
    @classmethod
    def make_slug(cls, title: str):
        return slugify(title)

    class Meta:
        __abstract__ = True
