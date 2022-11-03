from http import HTTPStatus
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends, Request
from fastapi.param_functions import Header
from starlette.middleware.cors import CORSMiddleware
from app.views import view_customer
from app.utils.entities.entity_customer import ResponseException

app = FastAPI(title="Integration Data",
    description="Integration Data",
    version="1.0.0",)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(ResponseException)
async def unicorn_exception_handler(request: Request, exc: ResponseException):
    """Handling exception when is of type ResponseException"""
    return JSONResponse(
        status_code=exc.status,
        content={"status":exc.status, "data": exc.data, "details":exc.details},
    )

@app.exception_handler(Exception)
async def catch_exceptions_middleware(request: Request, exc: ResponseException):
    """Handling exception when is of type Exception"""
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"status":HTTPStatus.INTERNAL_SERVER_ERROR, "data": [], "details":str(exc)},
    )

app.include_router(view_customer.router)