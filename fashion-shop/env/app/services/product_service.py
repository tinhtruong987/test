from sqlalchemy import text
from sqlalchemy.orm import Session
from app.models.product_model import Product
from app.views.product_view import ProductCreateSchema, ProductUpdateSchema

class ProductService:
    @staticmethod
    def product_get_all(db: Session):
        query = text("EXEC Product_GetAll")
        result = db.execute(query).fetchall()
        return [{"ProductID": row.ProductID, "Name": row.Name, "Price": row.Price, "ProductCode": row.ProductCode, "CategoryID": row.CategoryID, "Description": row.Description} for row in result]

    @staticmethod
    def product_read_by_id(db: Session, product_id: int):
        query = text("EXEC Product_ReadByID :ProductID")
        result = db.execute(query, {"ProductID": product_id})
        return result.fetchone()

    @staticmethod
    def product_create(db: Session, product_data: ProductCreateSchema):
        query = text("EXEC Product_Create :Name, :CategoryID, :Price, :Description")
        db.execute(query, {
            "Name": product_data.Name,
            "CategoryID": product_data.CategoryID,
            "Price": product_data.Price,
            "Description": product_data.Description
        })
        db.commit()

    @staticmethod
    def product_update(db: Session, product_data: ProductUpdateSchema):
        try:
            query = text("EXEC Product_Update :ProductID, :Name, :CategoryID, :Price, :Description")
            db.execute(query, {
                "ProductID": product_data.ProductID,
                "Name": product_data.Name,
                "CategoryID": product_data.CategoryID,
                "Price": product_data.Price,
                "Description": product_data.Description
            })
            db.commit()
        except Exception as e:
            db.rollback()
            raise ValueError(f"Failed to update product: {str(e)}")