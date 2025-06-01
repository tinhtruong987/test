from pydantic import BaseModel
from datetime import datetime

class OrderCreateSchema(BaseModel):
    CustomerID: int | None = None
    StaffID: int
    TotalAmount: float
    VoucherID: int | None = None
    DiscountAmount: float | None = 0
    Status: str | None = "Pending"

class OrderUpdateSchema(BaseModel):
    OrderID: int
    CustomerID: int | None = None
    StaffID: int | None = None
    TotalAmount: float | None = None
    VoucherID: int | None = None
    DiscountAmount: float | None = None
    Status: str | None = None

class OrderResponseSchema(BaseModel):
    OrderID: int
    CustomerID: int | None = None
    StaffID: int
    OrderDate: datetime
    TotalAmount: float
    VoucherID: int | None = None
    DiscountAmount: float | None = None
    Status: str
    IsActive: bool
    CreatedAt: datetime
    UpdatedAt: datetime | None = None

    class Config:
        from_attributes = True

class OrderItemCreateSchema(BaseModel):
    OrderID: int
    VariantID: int
    Quantity: int
    Price: float

class OrderItemResponseSchema(BaseModel):
    OrderItemID: int
    OrderID: int
    VariantID: int
    Quantity: int
    Price: float
    IsActive: bool
    CreatedAt: datetime
    UpdatedAt: datetime | None = None

    class Config:
        from_attributes = True
