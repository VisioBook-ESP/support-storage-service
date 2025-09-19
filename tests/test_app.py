import pytest
from fastapi.testclient import TestClient

from src import app

from tests.mocks.external_services import mock_database_service, mock_storage_service


# Exemple de fixture pytest pour injecter les mocks
@pytest.fixture
def override_dependencies(monkeypatch):
    monkeypatch.setattr(
        "app.dependencies.get_database_service", lambda: mock_database_service
    )
    monkeypatch.setattr(
        "app.dependencies.get_storage_service", lambda: mock_storage_service
    )
    return True


client = TestClient(app)


def test_upload_file(override_dependencies):
    response = client.post("/upload", files={"file": ("test.txt", b"test content")})
    assert response.status_code == 200
    assert response.json()["url"] == "mock-url"
