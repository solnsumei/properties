from typing import Optional
from pydantic import Field
from .baseschema import BaseSchema, NameDescriptionSchema


class InvestmentSchema(NameDescriptionSchema):
    min_amount: float = Field(..., gt=0)
    roi: float = Field(..., gt=0)
    duration: int = Field(..., gt=0, le=24)


class PropertySchema(NameDescriptionSchema):
    location: str = Field(..., min_length=3, max_length=50)
    plot_price: float = Field(..., gt=0)
    half_plot_price: Optional[float] = Field(None, lt=plot_price, gt=0)
    promo_price: Optional[float] = Field(None, lt=plot_price, gt=0)
    is_promo: bool

