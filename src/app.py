from fastapi import FastAPI

from src.handlers import health, health_db, storage

app = FastAPI()

app.include_router(health.router)
app.include_router(health_db.router, prefix="/health-db")
app.include_router(storage.router, prefix="/storage")
