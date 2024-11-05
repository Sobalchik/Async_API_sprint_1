import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    project_name: str = "mongo-api"

    mongodb_uri: str = "mongodb://localhost:27017"


settings = Settings(_env_file=".env")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
