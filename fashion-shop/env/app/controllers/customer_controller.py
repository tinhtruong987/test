from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.customer_service import CustomerService
from app.views.customer_view import CustomerResponseSchema, CustomerUpdatePointsSchema

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/{customer_id}", response_model=CustomerResponseSchema)
async def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    try:
        return CustomerService.get_customer_by_id(db, customer_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/Update")
async def update_customer_loyalty_points(data: CustomerUpdatePointsSchema, db: Session = Depends(get_db)):
    try:
        CustomerService.update_customer_loyalty_points(db, data.CustomerID, data.LoyaltyPoints)
        return {"message": "Customer loyalty points updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
