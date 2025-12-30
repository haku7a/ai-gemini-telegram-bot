import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from config import config
from handlers import router as main_router

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

dp = Dispatcher()


async def main() -> None:
    dp.include_router(main_router)

    bot = Bot(token=config.BOT_TOKEN.get_secret_value())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
