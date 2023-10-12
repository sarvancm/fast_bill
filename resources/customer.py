
from typing import List

from fastapi import APIRouter, Depends
from starlette.requests import Request

from managers.auth import oauth2_scheme
from managers.customer import CustomerManager
from schemas.request.agency import CustomerIn,SalesIn,SaleProductsIn
from schemas.response.agency import AgencyOut,CatOut



router = APIRouter(tags=["Customer"])






@router.get(
    "/api/core/customer/",
    dependencies=[Depends(oauth2_scheme)],
    # response_model=List[AgencyOut],
)

async def get_all_customer(request: Request):
   
    return await CustomerManager.get_all_customer()


@router.post(
    "/api/core/customer/",
    dependencies=[Depends(oauth2_scheme)],
    # response_model=CatOut,
)
async def create_customer(request: Request, complaint: CustomerIn):
    return await CustomerManager.create_customer(complaint.dict())


@router.get("/api/core/customer/{id}/",dependencies=[Depends(oauth2_scheme)],)
async def get_customer_by_id(request: Request, id: int):
    return await CustomerManager.get_customer_by_id(id)

@router.put(
    "/api/core/customer/{id}/",
    dependencies=[Depends(oauth2_scheme)],
)
async def update_customer(request: Request,id: int,agency:CustomerIn):
    await CustomerManager.update_customer(id,agency.dict())

@router.delete(
    "/api/core/customer/{id}/",
    dependencies=[Depends(oauth2_scheme),]
)
async def delete_customer(id: int):
    await CustomerManager.delete(id)
    return {'message':"success"}



@router.get(
    "/api/core/sales/",
    dependencies=[Depends(oauth2_scheme)],
    # response_model=List[AgencyOut],
)

async def get_all_sales(request: Request,):
   
    return await CustomerManager.get_all_sales()


@router.post(
    "/api/core/sales/",
    dependencies=[Depends(oauth2_scheme)],
   
)
async def create_sales(request: Request,sales:SalesIn,products:List[SaleProductsIn]):
    return await CustomerManager.create_sales(sales.dict(),products,)