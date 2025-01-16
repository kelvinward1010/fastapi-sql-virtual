import secrets
from pydantic import (
    AnyUrl,
    HttpUrl
)
from pydantic_settings import BaseSettings
from typing import List, Literal

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_HOST: str = "localhost"
    BACKEND_CORS_ORIGINS: List[AnyUrl] = []
    DOMAIN: str = "localhost"
    ENVIRONMENT: Literal["local", "development", "staging", "production"] = "local"

    DATABASE_URL: str = "postgresql+asyncpg://myuser:mypassword@localhost/mydatabase"


    PROJECT_NAME: str = "Fastapi Virtual"
    SENTRY_DSN: HttpUrl | None = None

    class Config:
        env_file = "../.env"

settings = Settings()
