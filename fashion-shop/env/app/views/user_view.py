from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserAccountCreateSchema(BaseModel):
    Username: str
    PasswordHash: str
    Email: EmailStr
    Role: str
    IsActive: Optional[bool] = True
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None



class UserAccountUpdateSchema(BaseModel):
    UserAccountID: int
    Username: Optional[str] = None
    PasswordHash: Optional[str] = None
    Email: Optional[EmailStr] = None
    Role: Optional[str] = None
    IsActive: Optional[bool] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class UserAccountResponseSchema(BaseModel):
    UserAccountID: int
    Username: str
    PasswordHash: str
    Email: EmailStr
    Role: str
    IsActive: bool
    CreatedAt: datetime
    UpdatedAt: Optional[datetime] = None

    class Config:
        from_attributes = True

