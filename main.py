import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from config import config
from handlers import router as main_router

from integrations.gemini.service import GeminiService

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

dp = Dispatcher()


async def main() -> None:
    dp.include_router(main_router)

    gemini_service = GeminiService(
        api_key=config.GEMINI_API_KEY.get_secret_value(), model=config.GEMINI_MODEL
    )

    bot = Bot(token=config.BOT_TOKEN.get_secret_value())

    await dp.start_polling(bot, config=config, gemini=gemini_service)


if __name__ == "__main__":
    asyncio.run(main())
