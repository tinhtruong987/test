from app.database import Base
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, Boolean
from sqlalchemy import func

class Order(Base):
    __tablename__ = "Orders"

    OrderID = Column(Integer, primary_key=True, index=True)
    CustomerID = Column(Integer, ForeignKey("Customers.CustomerID"), nullable=True)
    StaffID = Column(Integer, ForeignKey("Staff.StaffID"), nullable=False)
    OrderDate = Column(DateTime, default=func.now())
    TotalAmount = Column(Numeric(12, 2), nullable=False)
    VoucherID = Column(Integer, ForeignKey("Vouchers.VoucherID"), nullable=True)
    DiscountAmount = Column(Numeric(12, 2), default=0)
    Status = Column(String(20), default="Pending")
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime, default=func.now())
    UpdatedAt = Column(DateTime, nullable=True)

class OrderItem(Base):
    __tablename__ = "OrderItems"

    OrderItemID = Column(Integer, primary_key=True, index=True)
    OrderID = Column(Integer, ForeignKey("Orders.OrderID"), nullable=False)
    VariantID = Column(Integer, ForeignKey("ProductVariants.VariantID"), nullable=False)
    Quantity = Column(Integer, nullable=False)
    Price = Column(Numeric(12, 2), nullable=False)
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime, default=func.now())
    UpdatedAt = Column(DateTime, nullable=True)
