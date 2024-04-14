import json
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import bot_settings
from schemas import RequestSchema


dp = Dispatcher()


@dp.message(CommandStart())
async def handler_start(message: Message):
    await message.answer(f"Привет! Я бот-агрегатор.")


@dp.message()
async def handle_message(message: Message):
    if message.text:
        data = json.loads(message.text)
        request = RequestSchema(**data)
        print(request)
    else:
        await message.answer("Некорректный JSON документ")


async def main():
    bot = Bot(token=bot_settings.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
