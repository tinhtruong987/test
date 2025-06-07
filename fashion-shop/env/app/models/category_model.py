from app.database import Base
from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime, ForeignKey, Boolean
from sqlalchemy import func

class Category(Base):
    __tablename__ = "Category"

    CategoryID = Column(Integer, primary_key=True, index=True)
    CategoryName = Column(String(100), nullable=False)
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime, default=datetime.utcnow)
    UpdatedAt = Column(DateTime, nullable=True)