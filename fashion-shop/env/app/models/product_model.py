from app.database import Base
from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime, ForeignKey, Boolean
from sqlalchemy import func

class Product(Base):
    __tablename__ = "Products"

    ProductID = Column(Integer, primary_key=True, index=True)
    ProductCode = Column(String(20), unique=True, index=True)
    Name = Column(String(255), nullable=False, index=True)
    CategoryID = Column(Integer, ForeignKey("Category.CategoryID"))
    Price = Column(Numeric(12, 2), nullable=False)
    Description = Column(Text)
    IsActive = Column(Integer, default=1)
    CreatedAt = Column(DateTime, default=func.now())
    UpdatedAt = Column(DateTime, nullable=True)

class Category(Base):
    __tablename__ = "Category"

    CategoryID = Column(Integer, primary_key=True, index=True)
    CategoryName = Column(String(100), nullable=False)
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime, default="GETDATE()")
    UpdatedAt = Column(DateTime, nullable=True)