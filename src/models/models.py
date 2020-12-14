from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise import fields
from .appbasemodel import SluggableModel


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


PropertyPydantic = pydantic_model_creator(Property, name="Property")
InvestmentPydantic = pydantic_model_creator(Investment, name="Investment")