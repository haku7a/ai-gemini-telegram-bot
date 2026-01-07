import logging
from google import genai
from google.genai import types
from .presets import GenerationPresets

logger = logging.getLogger(__name__)


class TextService:
    def __init__(self, client: genai.Client, model: str):
        self.client = client
        self.model = model

    async def generate(
        self, prompt: str, config: types.GenerateContentConfig = None
    ) -> str:

        if config is None:
            config = GenerationPresets.default()

        try:
            chat = self.client.aio.chats.create(model=self.model)

            chat = await chat.send_message(
                prompt,
                config=config,
            )

            return chat.text

        except Exception as e:
            logger.error(f"Error during content generation: {e}")
            return "⚠️Ошибка при обращении к нейросети."
