from pydantic import BaseModel
from datetime import datetime

class CategoryCreateSchema(BaseModel):
    CategoryName: str

class CategoryUpdateSchema(BaseModel):
    CategoryID: int
    CategoryName: str | None = None

class CategoryResponseSchema(BaseModel):
    CategoryID: int
    CategoryName: str
    IsActive: bool
    CreatedAt: datetime
    UpdatedAt: datetime | None = None

    class Config:
        from_attributes = True