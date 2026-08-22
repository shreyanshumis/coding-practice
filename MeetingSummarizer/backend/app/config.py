from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    groq_api_key: str = ""
    ai_provider: str = "groq"
    transcription_model: str = "whisper-large-v3-turbo"
    summary_model: str = "openai/gpt-oss-20b"
    database_url: str = "sqlite:///./meeting_summarizer.db"
    upload_directory: str = "uploads"
    max_upload_mb: int = 25
    frontend_origin: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=(".env", "backend/.env"), extra="ignore")

    @property
    def upload_path(self) -> Path:
        path = Path(__file__).resolve().parents[2] / self.upload_directory
        return path.resolve()


settings = Settings()
