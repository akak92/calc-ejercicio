from fastapi import APIRouter, HTTPException, Query
from typing import Union
from src.models.models import Calculadora
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
calc = Calculadora()

@router.get("/suma")
def suma(a: Union[int, float] = Query(...), b: Union[int, float] = Query(...)) -> dict:
    """
    Suma dos números.
    
    Parameters
    ----------
    a : int or float
        Primer sumando.
    b : int or float
        Segundo sumando.
    
    Returns
    -------
    dict
        Resultado de la suma.
    """
    try:
        resultado = calc.suma(a, b)
        return {"resultado": resultado}
    except TypeError as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/resta")
def resta(a: Union[int, float] = Query(...), b: Union[int, float] = Query(...)) -> dict:
    """
    Resta dos números.
    ...
    """
    try:
        resultado = calc.resta(a, b)
        return {"resultado": resultado}
    except TypeError as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/producto")
def producto(a: Union[int, float] = Query(...), b: Union[int, float] = Query(...)) -> dict:
    """
    Multiplica dos números.
    ...
    """
    try:
        resultado = calc.producto(a, b)
        return {"resultado": resultado}
    except TypeError as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/division")
def division(a: Union[int, float] = Query(...), b: Union[int, float] = Query(...)) -> dict:
    """
    Divide dos números.
    ...
    """
    try:
        resultado = calc.division(a, b)
        return {"resultado": resultado}
    except (TypeError, ValueError) as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))
