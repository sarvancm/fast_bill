
from typing import List

from fastapi import APIRouter, Depends
from starlette.requests import Request

from managers.auth import oauth2_scheme
from managers.product import ProductManager
from schemas.request.agency import AgencyIn,CatIn,ProductIn
from schemas.response.agency import AgencyOut,CatOut



router = APIRouter(tags=["Product"])



@router.get(
    "/api/core/product/",
    dependencies=[Depends(oauth2_scheme)],
    # response_model=List[AgencyOut],
)

async def get_all_product(request: Request):
   
    return await ProductManager.get_all_product()


@router.post(
    "/api/core/product/",
    dependencies=[Depends(oauth2_scheme)],
    # response_model=CatOut,
)
async def create_product(request: Request, complaint: ProductIn):
    return await ProductManager.create_product(complaint.dict())


@router.get("/api/core/product/{id}/",dependencies=[Depends(oauth2_scheme)],)
async def get_product_by_id(request: Request, id: int):
    return await ProductManager.get_product_by_id(id)

@router.put(
    "/api/core/product/{id}/",
    dependencies=[Depends(oauth2_scheme)],
)
async def update_product(request: Request,id: int,agency:ProductIn):
    await ProductManager.update_product(id,agency.dict())

@router.delete(
    "/api/core/product/{id}/",
    dependencies=[Depends(oauth2_scheme),]
)
async def delete_category(id: int):
    await ProductManager.delete(id)
    return {'message':"success"}