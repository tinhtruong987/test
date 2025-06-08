from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ColorCreateSchema(BaseModel):
    ColorName: str
    IsActive: Optional[bool] = True

class ColorUpdateSchema(BaseModel):
    ColorID: int
    ColorName: str
    IsActive: Optional[bool] = True

class ColorResponseSchema(BaseModel):
    ColorID: int
    ColorName: str
    IsActive: bool
    CreatedAt: datetime
    UpdatedAt: Optional[datetime]
