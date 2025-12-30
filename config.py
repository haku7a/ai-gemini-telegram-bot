from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, field_validator
from typing import List


class Settings(BaseSettings):

    BOT_TOKEN: SecretStr
    GEMINI_API_KEY: SecretStr
    ALLOWED_USER_IDS: List[int]

    @field_validator("ALLOWED_USER_IDS", mode="before")
    @classmethod
    def parse_allowed_user_ids(cls, v):
        if isinstance(v, int):
            return [v]
        if isinstance(v, str):
            return [int(id_.strip()) for id_ in v.split(",") if id_.strip()]
        return v

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


config = Settings()
