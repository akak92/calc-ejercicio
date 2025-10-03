
import pytest
from fastapi.testclient import TestClient
import importlib.util
import sys
from pathlib import Path

# Cargar el módulo app.py dinámicamente
app_path = Path(__file__).parent.parent / "app.py"
spec = importlib.util.spec_from_file_location("app", str(app_path))
app_module = importlib.util.module_from_spec(spec)
sys.modules["app"] = app_module
spec.loader.exec_module(app_module)

client = TestClient(app_module.app)

def test_root():
    """Prueba el endpoint raíz de bienvenida."""
    response = client.get("/")
    assert response.status_code == 200
    assert "mensaje" in response.json()
    assert "bienvenido" in response.json()["mensaje"].lower()

def test_health():
    """Prueba el endpoint de health check."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_calc_suma():
    """Prueba el endpoint de suma."""
    response = client.get("/calc/suma?a=2&b=3")
    assert response.status_code == 200
    assert response.json()["resultado"] == 5

def test_calc_resta():
    """Prueba el endpoint de resta."""
    response = client.get("/calc/resta?a=5&b=2")
    assert response.status_code == 200
    assert response.json()["resultado"] == 3

def test_calc_producto():
    """Prueba el endpoint de producto."""
    response = client.get("/calc/producto?a=4&b=3")
    assert response.status_code == 200
    assert response.json()["resultado"] == 12

def test_calc_division():
    """Prueba el endpoint de división."""
    response = client.get("/calc/division?a=10&b=2")
    assert response.status_code == 200
    assert response.json()["resultado"] == 5

def test_calc_division_por_cero():
    """Prueba la división por cero (debe devolver error 400)."""
    response = client.get("/calc/division?a=10&b=0")
    assert response.status_code == 400
    assert "cero" in response.json()["detail"].lower()

def test_calc_tipo_invalido():
    """Prueba el manejo de tipos inválidos (debe devolver error 400)."""
    response = client.get("/calc/suma?a=uno&b=2")
    assert response.status_code == 422 or response.status_code == 400
