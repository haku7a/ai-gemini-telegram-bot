import logging
from google import genai
from google.genai import types
from .components.chat_manager import ChatManager
from .components.presets import GenerationPresets


logger = logging.getLogger(__name__)


class GeminiService:
    def __init__(self, api_key: str, model: str):
        self.client = genai.Client(api_key=api_key)
        self.model = model
        self.chat_manager = ChatManager(client=self.client, model=model)

    async def generate(
        self, prompt: str, user_id: int, config: types.GenerateContentConfig = None
    ) -> str:
        if config is None:
            config = GenerationPresets.default()

        try:

            chat = self.chat_manager.get_chat(user_id)

            response = await chat.send_message(prompt, config=config)

            return response.text
        except Exception as e:
            logger.error(f"Error service: {e}")
        return "⚠️ Ошибка при обращении к нейросети."

    def clear_history(self, user_id: int):
        self.chat_manager.clear_context(user_id)
