from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from utils.logger import setup_logging
import api.endpoints as endpoints
import exceptions.request_routes_exceptions as exception_routes


app = FastAPI()
logger = setup_logging()

logger.info("Bem vindo ao API Restful Python! Estou muito feliz por você estar aqui!")
logger.info("Inicializando API...")

app.include_router(endpoints.router)
app.add_exception_handler(Exception, exception_routes.generic_exception_handler)
app.add_exception_handler(RequestValidationError, exception_routes.validation_exception_handler)
