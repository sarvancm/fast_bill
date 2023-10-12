from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from asyncpg import UniqueViolationError
from db import database
from managers.auth import AuthManager
from models import user, RoleType,agency,productcat, productsubcat




class AgencyManager:
    @staticmethod
    async def create_agency(data):
        # async with database.transaction() as tconn:
        #     id_ = await tconn._connection.execute(agency.insert().values(data))
        #     # await AgencyManager.issue_transaction(tconn, data["amount"], f"{user['first_name']} {user['last_name']}", user["iban"], id_)
        # return await database.fetch_one(agency.select().where(agency.c.id == id_))
        try:
            id_ = await database.execute(agency.insert().values(**data))
        except IntegrityError as e:
            if isinstance(e.orig, UniqueViolationError):
                detail = ""
                if "uq_name_branch" in str(e.orig):
                    detail = "An agency with the same name and branch already exists."
                else:
                    detail = "A unique constraint violation occurred."

                raise HTTPException(status_code=400, detail=detail)
            else:
                raise HTTPException(status_code=500, detail="Internal server error")
        return {'message': 'success'}
    

    @staticmethod
    async def get_all_agency():
        return await database.fetch_all(agency.select())
    
    @staticmethod
    async def get_agency_by_id():
        return await database.fetch_one(agency.select().where(agency.c.id == id))
    
    @staticmethod
    async def update_agency(id,values):
        agency = await AgencyManager.get_agency_by_id(id)
        if not agency:
            raise HTTPException(status_code=404, detail="Agency not found")
        for field, value in values.items():
                if hasattr(agency, field):
                    setattr(agency, field, value)

        query = agency.update().where(agency.c.id == id).values(**values)
        await database.execute(query)
        return {'message': 'success'}


class CategoryManager:

    @staticmethod
    async def create_category(data):
        try:
            id_ = await database.execute(productcat.insert().values(**data))
        except UniqueViolationError:
            raise HTTPException(400, "Category Name already exists")
        user_do = await database.fetch_one(productcat.select().where(productcat.c.id == id_))
        return {'message': 'success'}

    @staticmethod
    async def get_all_category():
        return await database.fetch_all(productcat.select())
    

    @staticmethod
    async def get_category_by_id(id):
        return await database.fetch_one(productcat.select().where(productcat.c.id == id))

    @staticmethod
    async def update_category(id,values):
        agency = await CategoryManager.get_category_by_id(id)
        if not agency:
            raise HTTPException(status_code=404, detail="Category not found")
        for field, value in values.items():
                if hasattr(agency, field):
                    setattr(agency, field, value)

        query = productcat.update().where(productcat.c.id == id).values(**values)
        try:
            await database.execute(query)
            return {'message': 'success'}
        except UniqueViolationError:
            raise HTTPException(400, "Category Name already exists")
        

    @staticmethod
    async def delete(id):
        await database.execute(productcat.delete().where(productcat.c.id == id))
        

class SubCategoryManager:

    @staticmethod
    async def create_sub_category(data):
        try:
            id_ = await database.execute(productsubcat.insert().values(**data))
        except UniqueViolationError:
            raise HTTPException(400, "sub category name for category already exists")
        user_do = await database.fetch_one(productsubcat.select().where(productsubcat.c.id == id_))
        return {'message': 'success'}

    @staticmethod
    async def get_all_sub_category():
        return await database.fetch_all(productsubcat.select())
    

    @staticmethod
    async def get_sub_category_by_id(id):
        return await database.fetch_one(productsubcat.select().where(productsubcat.c.id == id))

    @staticmethod
    async def update_sub_category(id,values):
        agency = await SubCategoryManager.get_sub_category_by_id(id)
        if not agency:
            raise HTTPException(status_code=404, detail="not found")
        for field, value in values.items():
                if hasattr(agency, field):
                    setattr(agency, field, value)

        query = productsubcat.update().where(productsubcat.c.id == id).values(**values)
        try:
            await database.execute(query)
            return {'message': 'success'}
        except UniqueViolationError:
            raise HTTPException(400, "sub category name for category already exists")

    @staticmethod
    async def delete(id):
        await database.execute(productsubcat.delete().where(productsubcat.c.id == id))