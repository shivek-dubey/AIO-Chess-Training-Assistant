from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "AIO Chess Training Assistant")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")


settings = Settings()
