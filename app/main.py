from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from app.api.health import router as health_router
from app.db.database import create_db

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicializar la base de datos al arrancar
    try:
        create_db()
        logger.info("Base de datos inicializada correctamente.")
    except Exception as e:
        logger.error(f"Error al inicializar la base de datos: {e}")
    yield


app = FastAPI(title="Awards Service", version="1.0.0", lifespan=lifespan)

app.include_router(health_router)


@app.get("/")
def root():
    return {"service": "awards-service", "status": "online"}
