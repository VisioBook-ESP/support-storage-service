from fastapi import FastAPI
from src.handlers import storage

app = FastAPI(title="Support Storage Service")

app.include_router(storage.router)

