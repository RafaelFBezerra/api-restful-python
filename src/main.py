from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from sqlalchemy.exc import IntegrityError

from utils.logger import setup_logging
import api.endpoints as endpoints
import exceptions.request_routes_exceptions as exception_routes


app = FastAPI()
logger = setup_logging()


logger.info("Bem vindo ao API Restful Python! Me sinto feliz por você estar aqui!")
logger.info("Inicializando API...")

app.include_router(endpoints.router)
app.add_exception_handler(IntegrityError, exception_routes.integrity_exception_handler)
app.add_exception_handler(RequestValidationError, exception_routes.validation_exception_handler)
app.add_exception_handler(Exception, exception_routes.generic_exception_handler)
app.add_exception_handler(HTTPException, exception_routes.http_exception_handler)
