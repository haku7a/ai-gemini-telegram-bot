from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

from filters.is_allowed_user import IsAllowedUser

router = Router()

router.message.filter(IsAllowedUser())


@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("😁")
