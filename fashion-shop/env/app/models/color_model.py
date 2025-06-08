from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import Base

class Color(Base):
    __tablename__ = "Colors"

    ColorID = Column(Integer, primary_key=True, index=True)
    ColorName = Column(String(50), nullable=False)
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime)
    UpdatedAt = Column(DateTime, nullable=True)
