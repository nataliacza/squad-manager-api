import os
from typing import List

from dotenv import load_dotenv
from pydantic import BaseSettings

from app.api import api_description

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = api_description.PROJECT_NAME
    PROJECT_DESCRIPTION: str = api_description.PROJECT_DESCRIPTION
    PROJECT_VERSION: str = api_description.PROJECT_VERSION
    API_TAGS: List = api_description.API_TAGS

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "0.0.0.0")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "api_db")
    TEST_DB: str = os.getenv("TEST_DB", "test_db")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    TEST_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{TEST_DB}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
