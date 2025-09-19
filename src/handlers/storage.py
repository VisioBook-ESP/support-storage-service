from fastapi import APIRouter, Depends, File, UploadFile

from src.dependencies import get_storage_service

router = APIRouter()

# Module-level singletons for dependency injection
file_dependency = File(...)
storage_service_dependency = Depends(get_storage_service)


@router.get("/items")
async def read_items() -> dict[str, list]:
    return {"items": []}


@router.post("/upload")
async def upload_file(
    file: UploadFile = file_dependency, storage_service=storage_service_dependency
) -> dict[str, str]:
    """Upload a file and return its URL."""
    # Use the storage service to upload the file
    result = await storage_service.upload_file(file)
    return result
