from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import func

class Size(Base):
    __tablename__ = "Sizes"

    SizeID = Column(Integer, primary_key=True, index=True)
    SizeName = Column(String(50), nullable=False)
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime, default=func.now(), nullable=True)
    UpdatedAt = Column(DateTime, nullable=True)
