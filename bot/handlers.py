import json

from aiogram import Router
from aiogram.types import Message
from pydantic import ValidationError

from bot import crud
from bot.schemas import RequestSchema
from bot.utils import make_dataset

router = Router(name=__name__)


@router.message()
async def handle_message(message: Message):
    if message.text is None:
        await message.answer("Некорректный формат сообщения!")
        return

    try:
        data = json.loads(message.text)
        request = RequestSchema(**data)
        payments = await crud.get_payments(request)
        dataset = make_dataset(payments)
        await message.answer(text=dataset.model_dump_json())
    except (ValidationError, json.decoder.JSONDecodeError) as e:
        await message.answer(
            'Допустимо отправлять только следующие запросы:'
            '{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}'
            '{"dt_from": "2022-10-01T00:00:00", "dt_upto": "2022-11-30T23:59:00", "group_type": "day"}'
            '{"dt_from": "2022-02-01T00:00:00", "dt_upto": "2022-02-02T00:00:00", "group_type": "hour"}'
        )