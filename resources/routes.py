from fastapi import APIRouter
from resources import auth,agency,product,customer

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(agency.router)
api_router.include_router(product.router)
api_router.include_router(customer.router)
