import pytest
from fastapi.testclient import TestClient

from src.app import app
from tests.mocks.external_services import (mock_database_service,
                                           mock_storage_service)


# Fixture pytest pour injecter les mocks
@pytest.fixture
def override_dependencies(monkeypatch):
    # Patch les fonctions get_database_service et get_storage_service
    monkeypatch.setattr(
        "src.app.dependencies.get_database_service",
        lambda: mock_database_service,
    )
    monkeypatch.setattr(
        "src.app.dependencies.get_storage_service",
        lambda: mock_storage_service,
    )
    return True


# Test client pour interagir avec l'app FastAPI
client = TestClient(app)


def test_upload_file(override_dependencies) -> None:
    """
    Teste l'endpoint POST /upload en utilisant les services mockés.
    """
    response = client.post(
        "/upload",
        files={"file": ("test.txt", b"test content")},
    )
    assert response.status_code == 200
    assert response.json()["url"] == "mock-url"