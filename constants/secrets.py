from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    RQUID: str = '9878'

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
