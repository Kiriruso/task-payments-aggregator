from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def handler_start(message: Message):
    await message.answer(f"Привет! Я бот-агрегатор.\nПринимаю данные в формате JSON")
