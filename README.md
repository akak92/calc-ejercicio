
# 🧮 Calculadora API

Una API de calculadora básica construida con FastAPI, que permite realizar operaciones aritméticas simples y consultar el estado de la aplicación y la base de datos MongoDB. El proyecto sigue buenas prácticas de desarrollo, validación y pruebas.

## 📑 Tabla de Contenidos
- [📝 Descripción](#descripción)
- [✨ Características](#características)
- [🛠️ Requisitos](#requisitos)
- [⚙️ Instalación](#instalación)
- [🔧 Configuración](#configuración)
- [🚀 Uso](#uso)
- [🔗 Endpoints](#endpoints)
- [🧪 Pruebas](#pruebas)
- [📁 Estructura del Proyecto](#estructura-del-proyecto)
- [📄 Licencia](#licencia)

## 📝 Descripción
Esta API expone operaciones matemáticas básicas (suma, resta, multiplicación, división) y endpoints de salud. Utiliza FastAPI y almacena resultados en MongoDB (configurable por variables de entorno).

## ✨ Características
- Operaciones aritméticas básicas vía endpoints REST.
- Validación de tipos y manejo de errores.
- Endpoints de salud para la app y la base de datos.
- Configuración segura mediante `.env`.
- Pruebas unitarias con pytest.
- Código organizado y documentado siguiendo PEP 8 y buenas prácticas.

## 🛠️ Requisitos
- Python 3.8+
- MongoDB (opcional, para endpoints de salud de base de datos)

## ⚙️ Instalación
```bash
# Clona el repositorio
$ git clone <url-del-repo>
$ cd calc-ejercicio

# Crea y activa un entorno virtual
$ python -m venv venv
$ .\venv\Scripts\activate  # En Windows

# Instala las dependencias
$ pip install -r requirements.txt
```

## 🔧 Configuración
Copia el archivo `.env` de ejemplo y ajusta las variables según tu entorno:
```env
MONGO_URI=mongodb://localhost:27017
MONGO_DB=calc_ejercicio
MONGO_COLLECTION=results
```

## 🚀 Uso
Inicia el servidor de desarrollo:
```bash
uvicorn app:app --reload
```
Accede a la documentación interactiva en: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🔗 Endpoints
### 🏠 Raíz
- `GET /` — Mensaje de bienvenida.

### ❤️ Salud
- `GET /health` — Estado de la API.
- `GET /db_health` — Estado de la conexión a MongoDB.

### ➗ Calculadora (`/calc`)
- `GET /calc/suma?a=2&b=3` — Suma dos números.
- `GET /calc/resta?a=5&b=2` — Resta dos números.
- `GET /calc/producto?a=4&b=3` — Multiplica dos números.
- `GET /calc/division?a=10&b=2` — Divide dos números.

## 🧪 Pruebas
Ejecuta las pruebas unitarias con pytest:
```bash
pytest
```

## 📁 Estructura del Proyecto
```
calc-ejercicio/
├── app.py                # App principal FastAPI
├── requirements.txt      # Dependencias
├── .env                  # Configuración de entorno
├── src/
│   ├── models/
│   │   └── models.py     # Lógica de la calculadora
│   └── routes/
│       └── calculator.py # Endpoints de la calculadora
├── tests/
│   └── test_endpoints.py # Pruebas unitarias
└── README.md
```

## 📄 Licencia
MIT
