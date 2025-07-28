from pydantic_settings import BaseSettings
from typing import List
import sys

class Settings(BaseSettings):
    app_name: str = "Astrogematría API - Astrowellness"
    version: str = "1.0.0"
    host: str = "0.0.0.0"
    port: int = 8003
    cors_origins: List[str] = ["http://localhost:3000"]
    log_level: str = "INFO"
    python_version: str = f"{sys.version_info.major}.{sys.version_info.minor}"

settings = Settings()
