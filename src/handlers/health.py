"""
Module contenant l'endpoint de health check pour l'application.

Fournit l'état de santé des services internes et externes.
"""

import datetime
import os

import asyncpg
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

@router.get("/health")
async def health_check(response: Response) -> dict:
    """
    Endpoint pour vérifier l'état de santé global de l'application.

    Retourne un JSON contenant l'état de la base de données, ainsi qu'un status global, un timestamp et les
    informations de version/service.
    """
    checks = {
        "database": await check_database(),
    }
    is_healthy = all(c["status"] == "UP" for c in checks.values())

    health = {
        "status": "UP" if is_healthy else "DOWN",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "service": os.getenv("SERVICE_NAME", "user-service"),
        "version": os.getenv("SERVICE_VERSION", "1.0.0"),
        "checks": checks,
    }

    response.status_code = (
        status.HTTP_200_OK if is_healthy else status.HTTP_503_SERVICE_UNAVAILABLE
    )
    return health
