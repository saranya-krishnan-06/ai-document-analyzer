from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Document Analyzer"
    MODEL_NAME: str = "google/flan-t5-small"
    MAX_NEW_TOKENS: int = 150

    class Config:
        env_file = ".env"


settings = Settings()