import os

# JSONPlaceholder: contratos POST/PUT y validacion de esquema (sin auth real).
JSONPLACEHOLDER_URL = os.getenv(
    "JSONPLACEHOLDER_URL",
    "https://jsonplaceholder.typicode.com",
)

# DummyJSON: autenticacion con tokens y credenciales de prueba.
DUMMYJSON_URL = os.getenv(
    "DUMMYJSON_URL",
    "https://dummyjson.com",
)

MAX_RESPONSE_TIME_SECONDS = float(
    os.getenv("API_MAX_RESPONSE_TIME", "1.5")
)
