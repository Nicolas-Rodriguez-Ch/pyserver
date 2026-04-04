from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    UUID: str = ""
    DB_URL: str = ""
    DB_URL_SYNC: str = ""
    DB_ECHO: bool = True

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
