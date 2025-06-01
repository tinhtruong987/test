from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.product_service import ProductService
from app.views.product_view import ProductCreateSchema, ProductUpdateSchema, ProductResponseSchema
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
async def product_get_all(db: Session = Depends(get_db)):
    return ProductService.product_get_all(db)

@router.get("/{product_id}")
async def product_read_by_id(product_id: int, db: Session = Depends(get_db)):
    return ProductService.product_read_by_id(db, product_id)

@router.post("/Create")
async def product_create(product_data: ProductCreateSchema, db: Session = Depends(get_db)):
    ProductService.product_create(db, product_data)
    return {"message": "Product created successfully"}

@router.put("/Update")
async def product_update(product_data: ProductUpdateSchema, db: Session = Depends(get_db)):
    ProductService.product_update(db, product_data)
    return {"message": "Product updated successfully"}