
from fastapi import APIRouter, HTTPException
from app.models import Product
from app.db.schemas import Product, ProductCreate
from tortoise.exceptions import DoesNotExist

router = APIRouter()

@router.post('/product', response_model=Product)
async def createProduct(product: ProductCreate):
    
    product_obj = await Product.create(**product.dict())
    return product_obj

@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    try:
        product_obj = await Product.get(id=product_id)
        return product_obj
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Product not found")

@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductCreate):
    try:
        product_obj = await Product.get(id=product_id)
        product_obj.name = product.name
        product_obj.price = product.price
        product_obj.stockQnt = product.stockQnt
        await product_obj.save()
        return product_obj
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/products/{product_id}", response_model=Product)
async def delete_product(product_id: int):
    try:
        product_obj = await Product.get(id=product_id)
        await product_obj.delete()
        return product_obj
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Product not found")