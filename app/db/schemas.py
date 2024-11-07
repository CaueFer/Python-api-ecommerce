from pydantic import BaseModel
from decimal import Decimal

class ProductBase(BaseModel):
    name: str
    price: Decimal
    stocktQnt: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    
    class Config:
        orm_mode = True