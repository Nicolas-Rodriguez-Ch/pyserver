from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from .base import async_session


class DatabaseManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __call__(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_manager = DatabaseManager(async_session)
