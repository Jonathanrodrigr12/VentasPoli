from fastapi import FastAPI
from fastapi.param_functions import Header
from starlette.middleware.cors import CORSMiddleware
from app.views import view_customer

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

app.include_router(view_customer.router)