from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.color_service import ColorService
from app.database import get_db
from app.views.color_view import ColorCreateSchema, ColorUpdateSchema

router = APIRouter(prefix="/colors", tags=["Colors"])

@router.get("/get-all")
def get_all_colors(db: Session = Depends(get_db)):
    return ColorService.color_get_all(db)

@router.get("/read-by-id/{color_id}")
def read_color_by_id(color_id: int, db: Session = Depends(get_db)):
    result = ColorService.color_read_by_id(db, color_id)
    if not result:
        raise HTTPException(status_code=404, detail="Color not found")
    return result

@router.post("/create")
def create_color(color_data: ColorCreateSchema, db: Session = Depends(get_db)):
    ColorService.color_create(db, color_data)
    return {"message": "Color created successfully"}

@router.put("/update")
def update_color(color_data: ColorUpdateSchema, db: Session = Depends(get_db)):
    ColorService.color_update(db, color_data)
    return {"message": "Color updated successfully"}

@router.delete("/delete/{color_id}")
def delete_color(color_id: int, db: Session = Depends(get_db)):
    ColorService.color_delete(db, color_id)
    return {"message": "Color deleted successfully"}
