# app/controllers/auth_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.views.auth_view import AuthLoginSchema
from app.services.auth_service import authService
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login(data: AuthLoginSchema, db: Session = Depends(get_db)):
    user = authService.login(db, data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Login successful", "username": user.Username, "role": user.Role}