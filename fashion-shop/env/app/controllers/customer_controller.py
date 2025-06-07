from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.customer_service import CustomerService
from app.views.customer_view import CustomerResponseSchema, CustomerUpdatePointsSchema, CustomerCreateSchema, CustomerUpdateSchema

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/{customer_id}", response_model=CustomerResponseSchema)
async def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    try:
        return CustomerService.get_customer_by_id(db, customer_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/Update-point")
async def update_customer_loyalty_points(data: CustomerUpdatePointsSchema, db: Session = Depends(get_db)):
    try:
        CustomerService.update_customer_loyalty_points(db, data.CustomerID, data.LoyaltyPoints)
        return {"message": "Customer loyalty points updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[CustomerResponseSchema])
async def get_all_customers(db: Session = Depends(get_db)):
    return CustomerService.customer_get_all(db)

@router.post("/Create")
async def create_customer(data: CustomerCreateSchema, db: Session = Depends(get_db)):
    CustomerService.customer_create(db, data)
    return {"message": "Customer created successfully"}

@router.put("/Update")
async def update_customer(data: CustomerUpdateSchema, db: Session = Depends(get_db)):
    try:
        CustomerService.customer_update(db, data)
        return {"message": "Customer updated successfully"}
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/Delete/{customer_id}")
async def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    try:
        CustomerService.customer_delete(db, customer_id)
        return {"message": "Customer deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/activate/{customer_id}")
async def activate_customer(customer_id: int, db: Session = Depends(get_db)):
    try:
        CustomerService.customer_activate(db, customer_id)
        return {"message": f"Customer {customer_id} activated successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))