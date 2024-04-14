from typing import Literal
from datetime import datetime
from pydantic import BaseModel, model_validator


class RequestSchema(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: Literal["hour", "day", "month"]

    @model_validator(mode="after")
    def validate_date(self):
        if self.group_type == "month" and 0 < (self.dt_upto.month - self.dt_from.month) < 12:
            return self

        if self.group_type == "day" and 0 < (self.dt_upto - self.dt_from).days < 31:
            return self

        if self.group_type == "hour" and 0 < (self.dt_upto - self.dt_from).seconds < 86400:
            return self

        raise ValueError


class PaymentSchema(BaseModel):
    value: int
    dt: datetime


class DatasetSchema(BaseModel):
    dataset: list[int]
    labels: list[datetime]
