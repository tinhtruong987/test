from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.size_service import sizeService
from app.views.size_view import SizeCreateSchema, SizeUpdateSchema, SizeResponseSchema
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

router = APIRouter(prefix="/sizes", tags=["Sizes"])

@router.get("/")
async def size_get_all(db: Session = Depends(get_db)):
    return sizeService.size_get_all(db)

@router.get("/{size_id}")
async def size_read_by_id(size_id: int, db: Session = Depends(get_db)):
    size = sizeService.size_read_by_id(db, size_id)
    if not size:
        raise HTTPException(status_code=404, detail="Size not found")
    return size

@router.post("/Create")
async def size_create(size_data: SizeCreateSchema, db: Session = Depends(get_db)):
    logging.info(f"Creating size with data: {size_data}")
    sizeService.size_create(db, size_data)
    return {"message": "Size created successfully"}

@router.put("/Update")
async def size_update(size_data: SizeUpdateSchema, db: Session = Depends(get_db)):
    logging.info(f"Updating size with data: {size_data}")
    sizeService.size_update(db, size_data)
    return {"message": "Size updated successfully"}

@router.delete("/{size_id}")
async def size_delete(size_id: int, db: Session = Depends(get_db)):
    try:
        sizeService.size_delete(db, size_id)
        return {"message": "Size deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
