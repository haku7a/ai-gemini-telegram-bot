import logging
from google import genai
from google.genai import types
from .components.text_service import TextService


logger = logging.getLogger(__name__)


class GeminiService:
    def __init__(self, api_key: str, model: str):
        self.client = genai.Client(api_key=api_key)
        self.model = model

        self.text = TextService(client=self.client, model=model)

    async def generate(
        self, prompt: str, config: types.GenerateContentConfig = None
    ) -> str:

        return await self.text.generate(prompt=prompt, config=config)
