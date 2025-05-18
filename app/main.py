from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Currency Converter API")

app.include_router(router)