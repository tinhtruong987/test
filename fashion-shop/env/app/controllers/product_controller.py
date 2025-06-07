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
    print(f"Updating product with data: {product_data}")
    ProductService.product_create(db, product_data)
    return {"message": "Product created successfully"}

@router.put("/Update")
async def product_update(product_data: ProductUpdateSchema, db: Session = Depends(get_db)):
    print(f"Updating product with data: {product_data}")
    ProductService.product_update(db, product_data)
    return {"message": "Product updated successfully"}

@router.delete("/Delete/{product_id}")
async def product_delete(product_id: int, db: Session = Depends(get_db)):
    try:
        ProductService.product_delete(db, product_id)
        return {"message": f"Product with ID '{product_id}' was deleted successfully."}
    except ValueError as e:
        logging.error(f"Error deleting product: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/FilterByCategory/{category_id}")
async def filter_by_category(category_id: int, db: Session = Depends(get_db)):
    try:
        products = ProductService.product_filter_by_category(db, category_id)
        return products
    except ValueError as e:
        logging.error(f"Error filtering products: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/Restore/{product_id}")
async def product_restore(product_id: int, db: Session = Depends(get_db)):
    try:
        ProductService.product_restore(db, product_id)
        return {"message": f"Product with ID '{product_id}' was restored successfully."}
    except ValueError as e:
        logging.error(f"Error restoring product: {e}")
        raise HTTPException(status_code=400, detail=str(e))
