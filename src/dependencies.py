"""Dependencies for the application."""

import os
from typing import Any


def get_database_service() -> Any | None:
    """Get database service instance."""
    # For now, return a mock or placeholder
    if os.getenv("APP_ENV") == "test":
        try:
            from tests.mocks.external_services import mock_database_service

            return mock_database_service
        except ImportError:
            pass
    # TODO: Implement real database service
    return None


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
