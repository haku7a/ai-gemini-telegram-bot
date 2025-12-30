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

        fill_response = []
        try:
            async for chunk in await self.client.aio.models.generate_content_stream(
                model=self.model,
                contents=prompt,
                config=config,
            ):
                if chunk.text:
                    fill_response.append(chunk.text)

            return "".join(fill_response)
        except Exception as e:
            logger.error(f"Error during content generation: {e}")
            return "⚠️Ошибка при обращении к нейросети."
