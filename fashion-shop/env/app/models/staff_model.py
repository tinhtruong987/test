from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy import func

class Staff(Base):
    __tablename__ = "Staff"

    StaffID = Column(Integer, primary_key=True, index=True)
    UserAccountID = Column(Integer, ForeignKey("UserAccount.UserAccountID"), nullable=False)
    Name = Column(String(100), nullable=False)
    Position = Column(String(50), nullable=True)
    IsActive = Column(Boolean, nullable=True)
    CreatedAt = Column(DateTime, default=func.now(), nullable=True)
    UpdatedAt = Column(DateTime, nullable=True)

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