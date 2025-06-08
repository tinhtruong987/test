from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema để tạo mới một size
class SizeCreateSchema(BaseModel):
    SizeName: str
    IsActive: Optional[bool] = True

# Schema để cập nhật một size
class SizeUpdateSchema(BaseModel):
    SizeID: int
    SizeName: Optional[str] = None
    IsActive: Optional[bool] = None

# Schema để trả về dữ liệu size
class SizeResponseSchema(BaseModel):
    SizeID: int
    SizeName: str
    IsActive: bool
    CreatedAt: datetime
    UpdatedAt: Optional[datetime] = None

    class Config:
        from_attributes = True 
