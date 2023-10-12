# from schemas.base import UserBase
from pydantic import BaseModel, validator
from typing import List
class AgencyIn(BaseModel):
    name: str
    email: str
    branch: str
    address_1: str
    address_2: str
    city: str
    state: str
    gstin: str
    district: str


class CustomerIn(BaseModel):
    name: str
    email: str
    mobile_number: int
    address_1: str
    address_2: str
    district: str
    state: str
    pin: str
    district: str
    
class CatIn(BaseModel):
    name: str
    
class SubCatIn(BaseModel):
    category: int
    name: str

class ProductIn(BaseModel):
    name: str
    units: str
    price: float
    discount: float
    tax: str
    description: str
    hsn: str
    brand: str
    category: int
    sub_category: int

    @validator("price", pre=True, always=True)
    def validate_price(cls, value):
        return round(value, 2)
    
    @validator("discount", pre=True, always=True)
    def validate_discount(cls, value):
        return round(value, 2)

class SalesIn(BaseModel):
    mobile_number: int
    name: str
    balance: float
    total: float
    given_amount: float
    email: str
    customer: int


class SaleProductsIn(BaseModel):
    units: str
    quantity: int
    price: float
    product: int


class CreateSalesInput(BaseModel):
    sales: SalesIn
    products: List[SaleProductsIn]
    # @validator("balance", pre=True, always=True)
    # def validate_price(cls, value):
    #     return round(value, 2)
    
    # @validator("total", pre=True, always=True)
    # def validate_discount(cls, value):
    #     return round(value, 2)
    
    # @validator("given_amount", pre=True, always=True)
    # def validate_discount(cls, value):
    #     return round(value, 2)

# from pydantic_sqlalchemy import sqlalchemy_to_pydantic
# from models import agency 

# CustomerIn = sqlalchemy_to_pydantic(agency, exclude=["id", "created_at", "updated_at"])
