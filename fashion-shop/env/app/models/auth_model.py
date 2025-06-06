# app/models/auth_model.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import Base

class UserAccount(Base):
    __tablename__ = "UserAccount"
    __table_args__ = {"extend_existing": True}  # thêm dòng này để cho phép định nghĩa lại bảng

    UserAccountID = Column(Integer, primary_key=True, index=True)
    Username = Column(String(50), unique=True, index=True, nullable=False)
    PasswordHash = Column(String(255), nullable=False)
    Email = Column(String(100), unique=True, index=True, nullable=False)
    Role = Column(String(20), nullable=False)
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime)
    UpdatedAt = Column(DateTime, nullable=True)