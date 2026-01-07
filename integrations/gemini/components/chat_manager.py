from cachetools import TTLCache
from google import genai


class ChatManager:
    def __init__(self, client: genai.Client, model: str):
        self.client = client
        self.model = model

        self._chats = TTLCache(maxsize=200, ttl=3600)

    def get_chat(self, user_id: int):
        if user_id not in self._chats:
            self._chats[user_id] = self.client.aio.chats.create(model=self.model)
        return self._chats[user_id]

    def clear_context(self, user_id: int):
        if user_id in self._chats:
            del self._chats[user_id]
