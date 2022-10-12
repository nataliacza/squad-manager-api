import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic import BaseSettings

from app.core import api_description

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    PROJECT_NAME: str = api_description.PROJECT_NAME
    PROJECT_DESCRIPTION: str = api_description.PROJECT_DESCRIPTION
    PROJECT_VERSION: str = api_description.PROJECT_VERSION
    API_TAGS: List = api_description.API_TAGS

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "api_db")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    class Config:
        case_sensitive = True
        env_file = "/.env"

settings = Settings()
