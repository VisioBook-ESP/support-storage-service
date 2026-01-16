"""
Adapters pour les intégrations externes.

Modules:
    - azure_blob_adapter: Intégration Azure Blob Storage
    - azure_vision_adapter: Intégration Azure Vision API
    - azure_cdn_adapter: Intégration Azure CDN
    - database_adapter: Intégration core-database-service
"""

from .azure_blob_adapter import AzureBlobAdapter
from .azure_vision_adapter import AzureVisionAdapter, OCRResponse
from .azure_cdn_adapter import AzureCDNAdapter
from .database_adapter import DatabaseAdapter

__all__ = [
    'AzureBlobAdapter',
    'AzureVisionAdapter',
    'OCRResponse',
    'AzureCDNAdapter',
    'DatabaseAdapter',
]

