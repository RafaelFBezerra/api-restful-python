import os


DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "base_geral")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "A1p1ha-K3yl0g_J4uL3Z-W9n7X")

ENCODER_DECODER_ALGORITHM = "HS256"
TOKEN_EXPIRES_MINUTES = 30
TOKEN_AUTH = os.getenv("TOKEN_AUTH", "3a58fb16-f1c6-41bb-9c33-489e26f03bf0")

USERS_DB = {
    DB_USER: {
        "username": DB_USER,
        "hashed_password": DB_PASSWORD,
        "role": "admin"
    },
}

BASE_URL_API_CONSUMER = "https://fakestoreapi.com/products"
