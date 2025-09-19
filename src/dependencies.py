"""Dependencies for the application."""

import os


def get_database_service():
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


def get_storage_service():
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
