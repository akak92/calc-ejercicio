from fastapi import FastAPI
from typing import Dict
import logging

logger = logging.getLogger("uvicorn")

app: FastAPI = FastAPI()


@app.get("/health", response_model=Dict[str, str])
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