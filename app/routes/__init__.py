
from fastapi import APIRouter
from app.routes import products

router = APIRouter()

router.include_router(products.router)