
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from asyncpg import UniqueViolationError
from db import database
from managers.auth import AuthManager
from models import product



class ProductManager:

    @staticmethod
    async def create_product(data):
        try:
            id_ = await database.execute(product.insert().values(**data))
        except UniqueViolationError:
            raise HTTPException(400, "category ,sub category,brand, name for product already exists")
        user_do = await database.fetch_one(product.select().where(product.c.id == id_))
        return  {'message': 'success'}

    @staticmethod
    async def get_all_product():
        return await database.fetch_all(product.select())
    

    @staticmethod
    async def get_product_by_id(id):
        return await database.fetch_one(product.select().where(product.c.id == id))

    @staticmethod
    async def update_product(id,values):
        agency = await ProductManager.get_product_by_id(id)
        if not agency:
            raise HTTPException(status_code=404, detail="not found")
        for field, value in values.items():
                if hasattr(agency, field):
                    setattr(agency, field, value)

        query = product.update().where(product.c.id == id).values(**values)
        try:
             await database.execute(query)
             return {'message': 'success'}
        except UniqueViolationError:
            raise HTTPException(400, "category ,sub category,brand, name for product already exists")

    @staticmethod
    async def delete(id):
        await database.execute(product.delete().where(product.c.id == id))