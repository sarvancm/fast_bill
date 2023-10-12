
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from asyncpg import UniqueViolationError
from db import database
from managers.auth import AuthManager
from models import customer,sales,sale_products,salesbalancepayment



class CustomerManager:

    @staticmethod
    async def create_customer(data):
        try:
            id_ = await database.execute(customer.insert().values(**data))
        except UniqueViolationError:
            raise HTTPException(400, "category ,sub category,brand, name for customer already exists")
        user_do = await database.fetch_one(customer.select().where(customer.c.id == id_))
        return  {'message': 'success'}

    @staticmethod
    async def get_all_customer():
        return await database.fetch_all(customer.select())
    

    @staticmethod
    async def get_customer_by_id(id):
        return await database.fetch_one(customer.select().where(customer.c.id == id))

    @staticmethod
    async def update_customer(id,values):
        agency = await CustomerManager.get_customer_by_id(id)
        if not agency:
            raise HTTPException(status_code=404, detail="not found")
        for field, value in values.items():
                if hasattr(agency, field):
                    setattr(agency, field, value)

        query = customer.update().where(customer.c.id == id).values(**values)
        try:
            await database.execute(query)
            return {'message': 'success'}
        except UniqueViolationError:
            raise HTTPException(400, "category ,sub category,brand, name for customer already exists")

    @staticmethod
    async def delete(id):
        await database.execute(customer.delete().where(customer.c.id == id))


    
    @staticmethod
    async def get_all_sales():
        return await database.fetch_all(sales.select())
    

    @staticmethod
    async def create_sales(sales_data, products_data):
        async with database.transaction():
            # Insert sales data into the 'sales' table
            sale_id = await database.execute(sales.insert().values(**sales_data))

            # Insert product data into the 'sale_products' table
            for product_data in products_data:
                product_data = product_data.dict()
                product_data['sales'] = sale_id
                await database.execute(sale_products.insert().values(**product_data))
            sales_obj=await database.fetch_one(sales.select().where(sales.c.id==sale_id))
            sales_obj=dict(sales_obj)
            balance_data = {'sales': sale_id,'balance': sales_obj['balance'],'total': sales_obj['total'],'given_amount':sales_obj['given_amount']}
            balance=await database.execute(salesbalancepayment.insert().values(**balance_data))
            # Fetch and return all sales data
            all_sales = await database.fetch_all(sales.select())
            return all_sales
        
    @staticmethod
    async def get_all_sales():
            all_sales = await database.fetch_all(sales.select())
            return_sales =[]
            for sale in all_sales:
                sale=dict(sale)
                sale["products"]=await database.fetch_all(sale_products.select().where(sale_products.c.sales == sale['id']))
                return_sales.append(sale)
            return return_sales