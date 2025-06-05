from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import func

class UserAccount(Base):
    __tablename__ = "UserAccount"

    UserAccountID = Column(Integer, primary_key=True, index=True)
    Username = Column(String(50), nullable=False)
    PasswordHash = Column(String(255), nullable=False)
    Email = Column(String(100), nullable=False)
    Role = Column(String(20), nullable=False)
    IsActive = Column(Boolean, nullable=False)
    CreatedAt = Column(DateTime, default=func.now(), nullable=True)
    UpdatedAt = Column(DateTime, nullable=True)