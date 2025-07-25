from typing import AsyncIterator, AsyncGenerator

import aiohttp
from dishka import Provider, Scope, from_context, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.db_helper import DataBaseHelper
from app.core.parser import Parser

# from app.core.service import ParserService
from app.core.settings import Settings


class ServiceProvider(Provider):
    scope = Scope.REQUEST
    settings = from_context(Settings, scope=Scope.APP)

    # service = provide(ParserService)
    # db = provide(AlchemyRepository, provides=IDBRepository)
    parser = provide(Parser)

    @provide
    async def get_http_session(self) -> AsyncIterator[aiohttp.ClientSession]:
        async with aiohttp.ClientSession() as session:
            yield session


class SQLAlchemyProvider(Provider):
    scope = Scope.APP
    settings = from_context(Settings)

    @provide
    async def get_database_helper(
        self,
        settings: Settings,
    ) -> DataBaseHelper:
        return DataBaseHelper(
            url=str(settings.db.url),
        )

    @provide(scope=Scope.REQUEST)
    async def get_async_session(
        self,
        database_helper: DataBaseHelper,
    ) -> AsyncGenerator[AsyncSession, None]:
        async with database_helper.session_factory() as session:
            yield session
