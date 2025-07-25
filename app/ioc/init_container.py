from dishka import AsyncContainer, make_async_container

from app.core.settings import Settings
from app.ioc.providers import ServiceProvider, SQLAlchemyProvider


def init_async_container(settings: Settings) -> AsyncContainer:
    container = make_async_container(
        SQLAlchemyProvider(),
        ServiceProvider(),
        context={
            Settings: settings,
        },
    )
    return container
