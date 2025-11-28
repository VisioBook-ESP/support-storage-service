from fastapi import APIRouter, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test_db"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
router = APIRouter()


@router.get("/")
def health_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            if result.scalar() == 1:
                return {"status: ok", "db: reachable"}
            else:
                raise HTTPException(status_code=500, detail="Unexpected DB response")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")

    health = {
        "status": "UP" if is_healthy else "DOWN",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "service": os.getenv("SERVICE_NAME", "user-service"),
        "version": os.getenv("SERVICE_VERSION", "1.0.0"),
    }
