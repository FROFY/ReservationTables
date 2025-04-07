from contextlib import asynccontextmanager
from typing import Callable, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.database.abstract_entities.abstract_base import async_session_maker


class DatabaseSessionManager:
    def __init__(self, session_maker: async_sessionmaker[AsyncSession]):
        self.session_maker = session_maker

    @asynccontextmanager
    async def create_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_maker() as session:
            try:
                yield session
            except Exception as e:
                print(f"Ошибка при выполнении запроса: {e}")
                raise
            finally:
                await session.close()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.create_session() as session:
            yield session

    @property
    def session_dependency(self) -> Callable:
        return Depends(self.get_session)


session_manager = DatabaseSessionManager(async_session_maker)
SessionDep = session_manager.session_dependency
