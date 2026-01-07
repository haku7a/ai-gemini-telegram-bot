from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram import Router, F
from aiogram.enums import ParseMode
from integrations.gemini.service import GeminiService
from integrations.gemini.components.presets import GenerationPresets

from filters.is_allowed_user import IsAllowedUser

router = Router()

router.message.filter(IsAllowedUser())


@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("😁")


@router.message(Command("search"))
async def search_handler(
    message: Message, command: CommandObject, gemini: GeminiService
):
    await message.bot.send_chat_action(message.chat.id, "typing")

    response = await gemini.generate(
        prompt=message.text,
        user_id=message.from_user.id,
        config=GenerationPresets.google_search(),
    )

    await message.answer(response)


@router.message(F.text)
async def chat_handler(message: Message, gemini: GeminiService):
    await message.bot.send_chat_action(message.chat.id, "typing")

    response = await gemini.generate(prompt=message.text, user_id=message.from_user.id)
    await message.answer(response)
