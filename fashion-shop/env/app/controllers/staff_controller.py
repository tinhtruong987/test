from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.staff_service import staffService
from app.views.staff_view import StaffCreateSchema, StaffUpdateSchema, StaffResponseSchema
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

router = APIRouter(prefix="/staffs", tags=["Staffs"])

@router.get("/")
async def staff_get_all(db: Session = Depends(get_db)):
    return staffService.staff_get_all(db)

@router.get("/{staff_id}")
async def staff_read_by_id(staff_id: int, db: Session = Depends(get_db)):
    return staffService.staff_read_by_id(db, staff_id)

@router.post("/Create")
async def staff_create(staff_data: StaffCreateSchema, db: Session = Depends(get_db)):
    print(f"Updating staff with data: {staff_data}")
    staffService.staff_create(db, staff_data)
    return {"message": "Staff created successfully"}

@router.put("/Update")
async def staff_update(staff_data: StaffUpdateSchema, db: Session = Depends(get_db)):
    print(f"Updating staff with data: {staff_data}")
    staffService.staff_update(db, staff_data)
    return {"message": "Staff updated successfully"}