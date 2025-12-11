"""Dependencies for the application."""

import os
from typing import Any, Optional

import asyncpg


class DatabaseService:
    """Service pour gérer les connexions à la base de données."""

    def __init__(self, database_url: str):
        """Initialize the database service with the given URL."""
        self.database_url = database_url
        self._pool: Optional[asyncpg.Pool] = None

    async def get_connection(self) -> asyncpg.Connection:
        """Obtient une connexion à la base de données."""
        if not self._pool:
            self._pool = await asyncpg.create_pool(self.database_url)
        return await self._pool.acquire()

    async def close(self) -> None:
        """Ferme le pool de connexions."""
        if self._pool:
            await self._pool.close()


# Instances globales des services
_db_service: Optional[DatabaseService] = None


def get_database_service() -> Optional[DatabaseService]:
    """Get database service instance."""
    global _db_service

    if os.getenv("APP_ENV") == "test":
        try:
            from tests.mocks.external_services import mock_database_service

            return mock_database_service
        except ImportError:
            pass

    # Service réel
    database_url = os.getenv("DATABASE_URL")
    if database_url and not _db_service:
        _db_service = DatabaseService(database_url)

    return _db_service


def get_storage_service() -> Any | None:
    """Get storage service instance."""
    # For now, return a mock or placeholder
    if os.getenv("APP_ENV") == "test":
        try:
            from tests.mocks.external_services import mock_storage_service

            return mock_storage_service
        except ImportError:
            pass
    # TODO: Implement real storage service
    return None
