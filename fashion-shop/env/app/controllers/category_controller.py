from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.category_service import CategoryService
from app.views.category_view import CategoryCreateSchema, CategoryUpdateSchema
import logging


router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/")
def category_get_all(db: Session = Depends(get_db)):
    categories = CategoryService.category_get_all(db)
    return categories

@router.get("/{category_id}")
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = CategoryService.category_get_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/Create")
def create_category(request: CategoryCreateSchema, db: Session = Depends(get_db)):
    success = CategoryService.category_create(db, request.CategoryName)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to create category")
    return {"message": "Category created successfully"}

@router.put("/Update")
def category_update(category_data: CategoryUpdateSchema, db: Session = Depends(get_db)):
    success = CategoryService.category_update(db, category_data)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to update category")
    return {"message": "Category updated successfully"}

@router.delete("/Delete/{category_id}")
def category_delete(category_id: int, db: Session = Depends(get_db)):
    success = CategoryService.category_delete(db, category_id)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to delete category")
    return {"message": "Category deleted successfully"}