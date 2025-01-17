from fastapi import APIRouter

from src.api.v1 import main as v1_routes

api_router = APIRouter()
api_router.include_router(v1_routes.api_router, prefix="/api/v1")
