from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.views.customer_view import CustomerCreateSchema, CustomerUpdateSchema

class CustomerService:
    @staticmethod
    def get_customer_by_id(db: Session, customer_id: int):
        query = text("EXEC Customer_GetByID :CustomerID")
        result = db.execute(query, {"CustomerID": customer_id}).fetchall()
        return result[0] if result else None

    @staticmethod
    def update_customer_loyalty_points(db: Session, customer_id: int, loyalty_points: int):
        query = text("EXEC Customer_UpdateLoyaltyPoints :CustomerID, :LoyaltyPoints")
        db.execute(query, {"CustomerID": customer_id, "LoyaltyPoints": loyalty_points})

    @staticmethod
    def customer_get_all(db: Session):
        query = text("EXEC Customer_GetAll")
        result = db.execute(query).mappings().all()
        return [dict(row) for row in result]
    
    @staticmethod
    def customer_create(db: Session, data: CustomerCreateSchema):
        query = text("EXEC Customer_Create :Name, :Phone, :Email, :Address, :LoyaltyPoints")
        db.execute(query, {
            "Name": data.Name,
            "Phone": data.Phone,
            "Email": data.Email,
            "Address": data.Address,
            "LoyaltyPoints":data.LoyaltyPoints
        })
        db.commit()

    @staticmethod
    def customer_update(db: Session, data: CustomerUpdateSchema):
        try:
            query = text("EXEC Customer_Update :CustomerID, :Name, :Phone, :Email, :Address, :LoyaltyPoints")
            db.execute(query, {
                "CustomerID": data.CustomerID,
                "Name": data.Name,
                "Phone": data.Phone,
                "Email": data.Email,
                "Address": data.Address,
                "LoyaltyPoints":data.LoyaltyPoints
            })
            db.commit()
        except Exception as e:
            db.rollback()
            raise ValueError(f"Failed to update customer: {str(e)}")
        
    @staticmethod
    def customer_delete(db: Session, customer_id: int):
        try:
            query = text("EXEC Customer_Delete :CustomerID")
            db.execute(query, {"CustomerID": customer_id})
            db.commit()
        except Exception as e:
            db.rollback()
            raise ValueError(f"Failed to delete customer: {str(e)}")
        
    @staticmethod
    def customer_activate(db: Session, customer_id: int):
        query = text("EXEC Customer_Activate :CustomerID")
        db.execute(query, {"CustomerID": customer_id})
        db.commit()

    