from pydantic import BaseModel
from datetime import datetime

class ProductCreateSchema(BaseModel):
    Name: str
    CategoryID: int | None = None
    Price: float
    Description: str

class ProductUpdateSchema(BaseModel):
    ProductID: int
    Name: str | None = None
    CategoryID: int | None = None
    Price: float | None = None
    Description: str | None = None

class ProductResponseSchema(BaseModel):
    ProductID: int
    ProductCode: str
    Name: str
    CategoryID: int | None = None
    Price: float
    Description: str | None = None
    IsActive: int
    CreatedAt: datetime
    UpdatedAt: datetime | None = None

    class Config:
        from_attributes = True
