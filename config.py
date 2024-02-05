from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str = "Awesome API"

    model_config = SettingsConfigDict(env_file=".env")
