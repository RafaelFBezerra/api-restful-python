from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError

from utils.build_json_responses import responses_builder


app = FastAPI()


@app.exception_handler(IntegrityError)
async def integrity_exception_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=400,
        content=responses_builder(
            status_code=400,
            status_message="Erro de integridade de dados",
            data=str(exc)
        )
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=responses_builder(
            status_code=422,
            status_message="Erro de validação de dados.",
            data=exc.errors()
        )
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=responses_builder(
            status_code=500,
            status_message="Internal Server Error",
            data=str(exc)
        )
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=responses_builder(
            status_code=exc.status_code,
            status_message="Bad Request",
            data=str(exc.detail)
        )
    )
