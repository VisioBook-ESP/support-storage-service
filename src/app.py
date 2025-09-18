from fastapi import FastAPI
from handlers.health import router as health_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(health_router)

