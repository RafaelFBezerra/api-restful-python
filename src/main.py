from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from sqlalchemy.exc import IntegrityError

import api.endpoints as endpoints
from utils.logger import setup_logging
from api.auth_router import get_auth_router
import exceptions.request_routes_exceptions as exception_routes


app = FastAPI(
    title="Projeto de API Restful Python",
    description="Documentação da API de Clientes e Produtos.",
    version="1.0.0"
)
logger = setup_logging()


logger.info("Bem vindo ao API Restful Python! Me sinto feliz por você estar aqui!")
logger.info("Inicializando API...")

app.include_router(get_auth_router(), prefix="/api/v1", tags=["Autenticação"])
app.include_router(endpoints.router, prefix="/api/v1", tags=["API de Clientes e Produtos"])
app.add_exception_handler(IntegrityError, exception_routes.integrity_exception_handler)
app.add_exception_handler(RequestValidationError, exception_routes.validation_exception_handler)
app.add_exception_handler(Exception, exception_routes.generic_exception_handler)
app.add_exception_handler(HTTPException, exception_routes.http_exception_handler)
