from typing import Literal
from datetime import datetime
from pydantic import BaseModel


class RequestSchema(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: Literal["hour", "day", "month"]


class AggregatedPaymentsSchema(BaseModel):
    _id: int
    total: int
    dt: datetime


class DatasetSchema(BaseModel):
    dataset: list[int]
    labels: list[datetime]
