from typing import Any

import pytest
from fastapi.testclient import TestClient

from src.app import app
from tests.mocks.external_services import mock_database_service, mock_storage_service


# Fixture pytest pour injecter les mocks
@pytest.fixture
def override_dependencies(monkeypatch: Any) -> None:
    """Patch les fonctions get_database_service et get_storage_service.

    Avec les mocks.
    """
    monkeypatch.setattr(
        "src.dependencies.get_database_service",
        lambda: mock_database_service,
    )
    monkeypatch.setattr(
        "src.dependencies.get_storage_service",
        lambda: mock_storage_service,
    )


# Test client pour interagir avec l'app FastAPI
client = TestClient(app)
