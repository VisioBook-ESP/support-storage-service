from unittest.mock import AsyncMock, MagicMock

# Mock base de données
mock_database_service = MagicMock()
mock_database_service.get_connection = AsyncMock(return_value="mock_connection")
mock_database_service.execute_query = AsyncMock(
    return_value=[{"id": 1, "name": "test"}]
)
mock_database_service.transaction = AsyncMock(return_value=None)

# Mock stockage (fichiers)
mock_storage_service = MagicMock()
mock_storage_service.upload_file = AsyncMock(return_value={"url": "mock-url"})
mock_storage_service.delete_file = AsyncMock(return_value=True)

# Mock services internes (Visiobook)
mock_visiobook_service = MagicMock()
mock_visiobook_service.create_booking = AsyncMock(return_value={"booking_id": 123})
mock_visiobook_service.cancel_booking = AsyncMock(return_value=True)
