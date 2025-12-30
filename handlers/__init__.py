from aiogram import Router
from . import user_commands

router = Router()

router.include_router(user_commands.router)
