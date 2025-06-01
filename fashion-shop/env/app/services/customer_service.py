from sqlalchemy.orm import Session
from sqlalchemy.sql import text

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
