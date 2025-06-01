from pydantic import BaseModel
from datetime import datetime

class CustomerResponseSchema(BaseModel):
    CustomerID: int
    Name: str
    Phone: str | None = None
    Email: str | None = None
    Address: str | None = None
    LoyaltyPoints: int
    IsActive: bool
    CreatedAt: datetime
    UpdatedAt: datetime | None = None

    class Config:
        from_attributes = True

class CustomerUpdatePointsSchema(BaseModel):
    CustomerID: int
    LoyaltyPoints: int
