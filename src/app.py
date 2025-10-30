from fastapi import FastAPI

from src.handlers import health, storage

app = FastAPI()

app.include_router(health.router, prefix="")
app.include_router(storage.router, prefix="/storage")  # pylint: disable=no-member
