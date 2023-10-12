from typing import List

from fastapi import APIRouter, Depends
from starlette.requests import Request

from managers.auth import oauth2_scheme
from managers.agency import AgencyManager,CategoryManager,SubCategoryManager
from schemas.request.agency import AgencyIn,CatIn,SubCatIn
from schemas.response.agency import AgencyOut,CatOut



router = APIRouter(tags=["Core"])


@router.get(
    "/api/core/agency/",
    dependencies=[Depends(oauth2_scheme)],
    response_model=List[AgencyOut],
)

# async def get_all_agency(request: Request):
#     agencies = await AgencyManager.get_all_agency()
#     success_msg = "Agencies retrieved successfully"
   
#     response_data = {"message": success_msg, "agencies": agencies}
#     return response_data
async def get_all_agency(request: Request):
   
    return await AgencyManager.get_all_agency()


@router.post(
    "/api/core/agency/",
    dependencies=[Depends(oauth2_scheme)],
    response_model=AgencyOut,
)
async def create_agency(request: Request, complaint: AgencyIn):
    return await AgencyManager.create_agency(complaint.dict())


@router.put(
    "/api/core/agency/{id}/",
    dependencies=[Depends(oauth2_scheme)],
)
async def update_agency(request: Request,id: int,agency:dict):
    await AgencyManager.update_agency(id,agency)


@router.delete(
    "/api/core/category/{id}/",
    dependencies=[Depends(oauth2_scheme),]
)
async def delete_category(id: int):
    await CategoryManager.delete(id)
    return {'message':"success"}

@router.get(
    "/api/core/category/",
    dependencies=[Depends(oauth2_scheme)],
    # response_model=List[AgencyOut],
)

async def get_all_category(request: Request):
   
    return await CategoryManager.get_all_category()


@router.post(
    "/api/core/category/",
    dependencies=[Depends(oauth2_scheme)],
    # response_model=CatIn,
)
async def create_category(request: Request, complaint: CatIn):
    return await CategoryManager.create_category(complaint.dict())

@router.put(
    "/api/core/category/{id}/",
    dependencies=[Depends(oauth2_scheme)],
)
async def update_category(request: Request,id: int,agency:dict):
    await CategoryManager.update_category(id,agency)

@router.delete(
    "/api/core/category/{id}/",
    dependencies=[Depends(oauth2_scheme),]
)
async def delete_category(id: int):
    await CategoryManager.delete(id)
    return {'message':"success"}



@router.get(
    "/api/core/subcategory/",
    dependencies=[Depends(oauth2_scheme)],
    # response_model=List[AgencyOut],
)

async def get_all_subcategory(request: Request):
   
    return await SubCategoryManager.get_all_sub_category()


@router.post(
    "/api/core/subcategory/",
    dependencies=[Depends(oauth2_scheme)],
    response_model=CatOut,
)
async def create_sub_category(request: Request, complaint: SubCatIn):
    return await SubCategoryManager.create_sub_category(complaint.dict())


@router.get("/api/core/subcategory/{id}/",dependencies=[Depends(oauth2_scheme)],)
async def get_sub_category_by_id(request: Request, id: int):
    return await SubCategoryManager.get_sub_category_by_id(id)

@router.put(
    "/api/core/subcategory/{id}/",
    dependencies=[Depends(oauth2_scheme)],
)
async def update_sub_category(request: Request,id: int,agency:dict):
    await SubCategoryManager.update_sub_category(id,agency)

@router.delete(
    "/api/core/subcategory/{id}/",
    dependencies=[Depends(oauth2_scheme),]
)
async def delete_category(id: int):
    await SubCategoryManager.delete(id)
    return {'message':"success"}