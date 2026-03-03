from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AI Document Analyzer"
    MODEL_NAME: str = "google/flan-t5-small"
    MAX_NEW_TOKENS: int = 150

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"  # ignore unknown env variables
    )


settings = Settings()