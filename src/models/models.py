from passlib.context import CryptContext
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise import fields
from .appbasemodel import SluggableModel, AppBaseModel


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(AppBaseModel):
    email = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=250)
    is_admin = fields.BooleanField(default=False)

    @classmethod
    async def find_by_email(cls, email):
        return await cls.filter(email=email).first()

    @staticmethod
    def generate_hash(password: str):
        return pwd_context.hash(password)

    @staticmethod
    def verify_hash(password: str, hashed_password: str):
        return pwd_context.verify(password, hashed_password)

    class PydanticMeta:
        exclude = ('password',)


class Property(SluggableModel):
    name = fields.CharField(max_length=50, unique=True)
    location = fields.CharField(max_length=50)
    description = fields.TextField()
    plot_price = fields.DecimalField(max_digits=18, decimal_places=2, null=True)
    half_plot_price = fields.DecimalField(max_digits=18, decimal_places=2, null=True)
    promo_price = fields.DecimalField(max_digits=5, decimal_places=2, null=True)
    is_promo = fields.BooleanField(default=False)
    image_url = fields.CharField(max_length=250)


class Investment(SluggableModel):
    name = fields.CharField(max_length=50, unique=True)
    description = fields.TextField()
    min_amount = fields.DecimalField(max_digits=18, decimal_places=2)
    roi = fields.DecimalField(max_digits=4, decimal_places=1, null=True)
    duration = fields.IntField()
    image_url = fields.CharField(max_length=250)


class Page(SluggableModel):
    name = fields.CharField(max_length=50, unique=True)
    content = fields.TextField()
    image_url = fields.CharField(max_length=250, null=True)


UserPydantic = pydantic_model_creator(User, name="User")
PropertyPydantic = pydantic_model_creator(Property, name="Property")
InvestmentPydantic = pydantic_model_creator(Investment, name="Investment")
PagePydantic = pydantic_model_creator(Page, name="Page")
