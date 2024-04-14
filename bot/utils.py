from datetime import datetime, timedelta

from bot.schemas import RequestSchema, AggregatedPaymentsSchema, DatasetSchema


def make_pipline(request: RequestSchema) -> list[dict]:
    groups = {
        "hour": {'$hour': '$dt'},
        "day": {'$dayOfMonth': '$dt'},
        "month": {'$month': '$dt'},
    }
    group = groups.get(request.group_type)

    if group is None:
        raise ValueError('Некорректный тип группы')

    return [
        {'$match': {'dt': {'$gte': request.dt_from, '$lte': request.dt_upto}}},
        {'$group': {
            '_id': group,
            'total': {'$sum': '$value'},
            'dt': {'$first': '$dt'}
        }},
        {'$sort': {'dt': 1}}
    ]


def make_dataset(payments: list[AggregatedPaymentsSchema]) -> DatasetSchema:
    dataset: dict[str, list[int | str]] = {
        "dataset": [],
        "labels": []
    }

    for payment in payments:
        dataset["dataset"].append(payment.total)
        dataset["labels"].append(payment.dt.replace(minute=0, microsecond=0).isoformat())

    return DatasetSchema(**dataset)
