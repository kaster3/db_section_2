import os
from pathlib import Path
from typing import Literal
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(slots=True)
class Logs:
    format: str
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "WARNING"


@dataclass(slots=True)
class Postgresql:
    url: str


@dataclass(slots=True)
class Links:
    url = "https://spimex.com/markets/oil_products/trades/results/"


class Settings:
    def __init__(self) -> None:
        self._load_config()
        self.logs = Logs(level=os.getenv("LOG_LEVEL"), format=os.getenv("FORMAT"))
        self.db = Postgresql(url=os.getenv("DB_URL"))
        self.links = Links()

    @staticmethod
    def _load_config() -> None:
        env_path = Path(__file__).parent.parent.parent / ".template.env"
        load_dotenv(env_path)


settings = Settings()
