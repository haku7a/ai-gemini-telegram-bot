from aiogram.filters import BaseFilter
from aiogram.types import Message
from config import Settings


class IsAllowedUser(BaseFilter):
    async def __call__(self, message: Message, config: Settings) -> bool:
        return message.from_user.id in config.ALLOWED_USER_IDS
