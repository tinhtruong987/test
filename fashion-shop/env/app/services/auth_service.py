# app/services/auth_service.py

from sqlalchemy.orm import Session
from app.models.auth_model import UserAccount

class AuthService:
    def login(self, db: Session, username: str, password: str):
        user = db.query(UserAccount).filter(
            UserAccount.Username == username,
            UserAccount.PasswordHash == password,
            UserAccount.IsActive == True
        ).first()
        if not user:
            return None
        return user

authService = AuthService()