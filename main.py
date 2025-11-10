import asyncio
from os import getenv

from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import user_commands

dp = Dispatcher()


async def main() -> None:
    dp.include_router(user_commands.router)

    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
