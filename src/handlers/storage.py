from fastapi import APIRouter, UploadFile, File, Depends

from src.dependencies import get_storage_service

router = APIRouter()


@router.get("/items")
async def read_items() -> dict[str, list]:
    return {"items": []}


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    storage_service=Depends(get_storage_service)
) -> dict[str, str]:
    """Upload a file and return its URL."""
    # Use the storage service to upload the file
    result = await storage_service.upload_file(file)
    return result
