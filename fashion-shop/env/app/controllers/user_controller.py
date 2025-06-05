from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.user_service import userService
from app.views.user_view import UserAccountCreateSchema, UserAccountUpdateSchema, UserAccountResponseSchema
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
async def user_get_all(db: Session = Depends(get_db)):
    return userService.user_get_all(db)

@router.get("/{user_id}")
async def user_read_by_id(user_id: int, db: Session = Depends(get_db)):
    return userService.user_read_by_id(db, user_id)

@router.post("/Create")
async def user_create(user_data: UserAccountCreateSchema, db: Session = Depends(get_db)):
    print(f"Updating user with data: {user_data}")
    userService.user_create(db, user_data)
    return {"message": "user created successfully"}

@router.put("/Update")
async def user_update(user_data: UserAccountUpdateSchema, db: Session = Depends(get_db)):
    print(f"Updating user with data: {user_data}")
    userService.user_update(db, user_data)
    return {"message": "user updated successfully"}