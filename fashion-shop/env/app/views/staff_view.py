from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StaffCreateSchema(BaseModel):
    userAccountID: int | None = None
    Name: str
    Position: Optional[str] = None

class StaffUpdateSchema(BaseModel):
    StaffID: int
    userAccountID: Optional[int] = None
    Name: Optional[str] = None
    Position: Optional[str] = None
    IsActive: Optional[bool] = None


class StaffResponseSchema(BaseModel):
    StaffID: int
    UserAccountID: int
    Name: str
    Position: Optional[str] = None
    IsActive: Optional[bool] = None
    CreatedAt: datetime
    UpdatedAt: Optional[datetime] = None

    class Config:
        from_attributes = True

