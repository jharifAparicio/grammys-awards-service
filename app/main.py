# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.health import router as health_router
from app.db.database import create_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(
    title="Awards Service",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(health_router)

@app.get("/")
def root():
    return {
        "service": "awards-service",
        "status": "online"
    }