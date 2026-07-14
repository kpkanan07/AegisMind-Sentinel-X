import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    PROJECT_NAME = "AegisMind-Sentinel"

    VERSION = "1.0.0"

    AI_THRESHOLD = 70

    LOG_LEVEL = "INFO"


settings = Settings()