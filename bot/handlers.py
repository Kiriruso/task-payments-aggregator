import json

from aiogram import Router
from aiogram.types import Message
from pydantic import ValidationError

from bot.schemas import RequestSchema

router = Router(name=__name__)


@router.message()
async def handle_message(message: Message):
    if message.text is None:
        await message.answer("Некорректный формат сообщения!")
        return

    data = json.loads(message.text)

    try:
        request = RequestSchema(**data)
    except ValidationError as e:
        print(e.errors()[0])
        await message.answer(
            'Допустимо отправлять только следующие запросы:'
            '{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}'
            '{"dt_from": "2022-10-01T00:00:00", "dt_upto": "2022-11-30T23:59:00", "group_type": "day"}'
            '{"dt_from": "2022-02-01T00:00:00", "dt_upto": "2022-02-02T00:00:00", "group_type": "hour"}'
        )
