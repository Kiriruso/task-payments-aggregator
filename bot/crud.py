from bot.db import payments_collection
from bot.schemas import RequestSchema, AggregatedPaymentsSchema
from bot.utils import make_pipline


async def get_payments(request: RequestSchema) -> list[AggregatedPaymentsSchema]:
    pipline = make_pipline(request)
    cursor = payments_collection.aggregate(pipline)
    return [
        AggregatedPaymentsSchema(**payment)
        for payment in await cursor.to_list(length=None)
    ]
