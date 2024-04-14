import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import bot_settings
from bot.handlers import router as router_handlers
from bot.commands import router as router_commands

dp = Dispatcher()
dp.include_routers(
    router_commands,
    router_handlers
)


async def main():
    bot = Bot(token=bot_settings.TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
