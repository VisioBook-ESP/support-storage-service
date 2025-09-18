"""
Module principal de l'application Support Storage Service.

Ce module initialise l'application FastAPI et inclut les routers des handlers.
"""

from fastapi import FastAPI
from src.handlers import storage

app = FastAPI(title="Support Storage Service")

app.include_router(storage.router)

