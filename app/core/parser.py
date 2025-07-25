import asyncio
import logging

from aiohttp import ClientError, ClientSession
from bs4 import BeautifulSoup

from app.core.settings import Settings


log = logging.getLogger(__name__)


class Parser:
    def __init__(self, settings: Settings, session: ClientSession) -> None:
        self.session = session
        self.settings = settings

    async def parse_page(self, url: str) -> BeautifulSoup:
        try:

            async with self.session.get(url=url, timeout=10) as response:
                response.raise_for_status()
                return BeautifulSoup(await response.text(), "lxml")

        except asyncio.TimeoutError:
            log.error("Время вышло по запросу %s", url)
        except ClientError as e:
            log.error("HTTP error while fetching %s: %s", url, e)
        except Exception as e:
            log.error("Неизвестная ошибка: %s", e.__class__.__name__)

    @staticmethod
    def get_docs_links(soup: BeautifulSoup) -> str:
        divs = soup.find_all("div", _class="accordeon-inner__wrap-item")
        print(divs)
        links = [div["href"] for div in divs]
        print(links)
