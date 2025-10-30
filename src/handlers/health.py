"""
Module contenant l'endpoint de health check pour l'application.

Fournit l'état de santé des services internes et externes.
"""

import datetime
import os

import asyncpg
import redis
from fastapi import APIRouter, Response, status

from src.dependencies import get_database_service

router = APIRouter()


async def check_database() -> dict[str, str]:
    """Vérifie la connectivité avec la base de données."""
    try:
        # Utiliser la vraie connexion à la base de données
        db_service = get_database_service()
        if db_service and hasattr(db_service, "get_connection"):
            connection = await db_service.get_connection()
            if connection:
                # Test simple de connectivité
                await connection.close()
                return {"status": "UP", "details": "Database connection successful"}
        # Fallback: connexion directe si DATABASE_URL est définie
        database_url = os.getenv("DATABASE_URL")
        if database_url:
            conn = await asyncpg.connect(database_url)
            await conn.close()
            return {"status": "UP", "details": "Database connection successful"}
        return {"status": "UP", "details": "Database reachable (mock)"}
    except Exception as e:
        return {"status": "DOWN", "details": f"Database connection failed: {e!s}"}


async def check_redis() -> dict[str, str]:
    """Vérifie la connectivité avec Redis."""
    try:
        redis_url = os.getenv("REDIS_URL", "redis://redis:6379")
        r = redis.from_url(redis_url)
        await r.ping()
        await r.close()
        return {"status": "UP", "details": "Redis connection successful"}
    except Exception as e:
        return {"status": "DOWN", "details": f"Redis connection failed: {e!s}"}


async def check_external_services() -> dict[str, str]:
    """Vérifie la disponibilité des services externes."""
    # TODO: Implémenter les vraies vérifications des services externes
    # Pour l'instant, on simule une vérification
    try:
        # Exemple: vérifier un service externe
        # response = httpx.get("https://api.external-service.com/health")
        # if response.status_code == 200:
        #     return {"status": "UP", "details": "External services available"}
        return {"status": "UP", "details": "External services available (mock)"}
    except Exception as e:
        return {"status": "DOWN", "details": f"External services unavailable: {e!s}"}


@router.get("/health")
async def health_check(response: Response) -> dict:
    """
    Endpoint pour vérifier l'état de santé global de l'application.

    Retourne un JSON contenant l'état de la base de données, Redis et des
    services externes, ainsi qu'un status global, un timestamp et les
    informations de version/service.
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
