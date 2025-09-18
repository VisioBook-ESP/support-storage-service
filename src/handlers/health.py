from fastapi import APIRouter, Response, status
from datetime import datetime
import os

router = APIRouter()

async def check_database():
    return {"status": "UP", "details": "Database reachable"}

async def check_redis():
    return {"status": "UP", "details": "Redis OK"}

async def check_external_services():
    return {"status": "DOWN", "details": "API externe non disponible"}

@router.get("/health")
async def health_check(response: Response):
    checks = {
        "database": await check_database(),
        "redis": await check_redis(),
        "externalServices": await check_external_services()
    }
    is_healthy = all(c["status"] == "UP" for c in checks.values())

    health = {
        "status": "UP" if is_healthy else "DOWN",
        "timestamp": datetime.utcnow().isoformat(),
        "service": os.getenv("SERVICE_NAME", "my-service"),
        "version": os.getenv("SERVICE_VERSION", "1.0.0"),
        "checks": checks
    }

    response.status_code = status.HTTP_200_OK if is_healthy else status.HTTP_503_SERVICE_UNAVAILABLE
    return health
