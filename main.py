import asyncio
from os import getenv

from aiogram import Bot, Dispatcher

from config import TOKEN

dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
