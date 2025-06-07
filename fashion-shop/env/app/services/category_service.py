from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import Optional
from app.views.category_view import CategoryUpdateSchema

class CategoryService:

    @staticmethod
    def category_get_all(db: Session):
        sql = text("EXEC dbo.Category_GetAll")
        result = db.execute(sql)
        rows = result.fetchall()
        categories = [dict(row._mapping) for row in rows]
        return categories

    @staticmethod
    def category_get_by_id(db: Session, category_id: int):
        sql = text("EXEC dbo.Category_ReadByID :CategoryID")
        result = db.execute(sql, {"CategoryID": category_id})
        row = result.fetchone()
        if row:
            return dict(row._mapping)
        return None

    @staticmethod
    def category_create(db: Session, category_name: str):
        sql = text("EXEC dbo.Category_Create :CategoryName")
        db.execute(sql, {"CategoryName": category_name})
        db.commit()
        return True

    @staticmethod
    def category_update(db: Session, category_data: CategoryUpdateSchema):
        try:
            # Giả sử stored procedure Category_Update có 2 tham số: CategoryID, CategoryName
            sql = text("EXEC dbo.Category_Update :CategoryID, :CategoryName")
            params = {
                "CategoryID": category_data.CategoryID,
                "CategoryName": category_data.CategoryName,
            }
            db.execute(sql, params)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def category_delete(db: Session, category_id: int):
        try:
            sql = text("EXEC dbo.Category_Delete :CategoryID")
            db.execute(sql, {"CategoryID": category_id})
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            raise e
   

