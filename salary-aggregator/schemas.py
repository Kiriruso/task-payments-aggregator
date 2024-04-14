from typing import Literal
from datetime import datetime
from pydantic import BaseModel


class PaymentSchema(BaseModel):
    value: int
    dt: datetime


class RequestSchema(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: Literal["hour", "day", "month"]


class DatasetSchema(BaseModel):
    dataset: list[int]
    labels: list[datetime]
