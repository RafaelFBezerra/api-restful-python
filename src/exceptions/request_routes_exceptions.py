from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from utils.build_json_responses import responses_builder


app = FastAPI()


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
