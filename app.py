

from fastapi import FastAPI, HTTPException
from src.routes.calculator import router as calculator_router
from typing import Dict
import logging
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("uvicorn")

app: FastAPI = FastAPI()

# Registrar rutas de calculadora
app.include_router(calculator_router, prefix="/calc", tags=["Calculadora"])

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "db_ejercicio")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "calculator")


@app.get("/health", response_model=Dict[str, str], tags=["Health"])
def health() -> Dict[str, str]:
    """
    Health check endpoint.

    Returns
    -------
    dict
        Dictionary with status information.
    """
    logger.info("Health check requested.")
    return {"status": "ok"}


@app.get("/db_health", response_model=Dict[str, str], tags=["Database"])
def db_health() -> Dict[str, str]:
    """
    Database health check endpoint.

    Returns
    -------
    dict
        Dictionary with database connection status.
    """
    logger.info("Database health check requested.")
    
    try:
        client = MongoClient(MONGO_URI)

        client.admin.command('ping')
        
        db = client[MONGO_DB]
        collections = db.list_collection_names()
        
        client.close()
        
        logger.info("Database connection successful.")
        return {
            "status": "ok",
            "database": MONGO_DB,
            "uri": MONGO_URI,
            "collections_count": str(len(collections))
        }
        
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        raise HTTPException(
            status_code=503,
            detail=f"Database connection failed: {str(e)}"
        )
    
# Endpoint raíz que da la bienvenida al usuario
@app.get("/", tags=["Root"])
def root() -> dict:
    """
    Endpoint raíz que da la bienvenida al usuario.

    Returns
    -------
    dict
        Mensaje de bienvenida.
    """
    logger.info("Bienvenida solicitada en el endpoint raíz.")
    return {"mensaje": "¡Bienvenido a la API de la Calculadora!"}