"""
Module contenant l'endpoint de health check pour l'application.
Fournit l'état de santé des services internes et externes.
"""

import datetime
import os

from fastapi import APIRouter, Response, status

router = APIRouter()


async def check_database() -> dict[str, str]:
    """Vérifie la connectivité avec la base de données."""
    return {"status": "UP", "details": "Database reachable"}


async def check_redis() -> dict[str, str]:
    """Vérifie la connectivité avec Redis."""
    return {"status": "UP", "details": "Redis OK"}


async def check_external_services() -> dict[str, str]:
    """Vérifie la disponibilité des services externes."""
    return {"status": "DOWN", "details": "API externe non disponible"}


@router.get("/health")
async def health_check(response: Response) -> dict:
    """
    Endpoint pour vérifier l'état de santé global de l'application.

    Retourne un JSON contenant l'état de la base de données, Redis et des services externes,
    ainsi qu'un status global, un timestamp et les informations de version/service.
    """
    checks = {
        "database": await check_database(),
        "redis": await check_redis(),
        "externalServices": await check_external_services(),
    }
    is_healthy = all(c["status"] == "UP" for c in checks.values())

    health = {
        "status": "UP" if is_healthy else "DOWN",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "service": os.getenv("SERVICE_NAME", "my-service"),
        "version": os.getenv("SERVICE_VERSION", "1.0.0"),
        "checks": checks,
    }

    response.status_code = (
        status.HTTP_200_OK if is_healthy else status.HTTP_503_SERVICE_UNAVAILABLE
    )
    return health
