import os


DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "base_geral")
DB_USER = os.getenv("DB_USER", "principal_admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "senha_testes")

BASE_URL_API_CONSUMER = "https://fakestoreapi.com/products"
