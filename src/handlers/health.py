"""
Module contenant l'endpoint de health check pour l'application.
Fournit l'état de santé des services internes et externes.
"""

import datetime
import os
from fastapi import APIRouter, Response, status

router = APIRouter()


@router.get("/health")
async def health_check(response: Response) -> dict:
    """
    Endpoint pour vérifier l'état de santé global de l'application.

    Retourne un JSON contenant l'état de la base de données (simulé ici),
    ainsi qu'un status global, un timestamp et les informations de version/service.
    """

    # Exemple de checks (vous pouvez ajouter des vérifications réelles)
    checks = {
        "database": {"status": "UP"},  # Remplacer par vrai check si nécessaire
        "cache": {"status": "UP"},
    }

    is_healthy = all(c["status"] == "UP" for c in checks.values())

    health = {
        "status": "UP" if is_healthy else "DOWN",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "service": os.getenv("SERVICE_NAME", "user-service"),
        "version": os.getenv("SERVICE_VERSION", "1.0.0"),
        "checks": checks,
    }

    response.status_code = (
        status.HTTP_200_OK if is_healthy else status.HTTP_503_SERVICE_UNAVAILABLE
    )
    return health
