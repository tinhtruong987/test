from sqlalchemy import text
from sqlalchemy.orm import Session
from app.views.size_view import SizeCreateSchema, SizeUpdateSchema

class sizeService:
    @staticmethod
    def size_get_all(db: Session):
        query = text("EXEC Sizes_GetAll")
        result = db.execute(query).fetchall()
        return [
            {
                "sizeID": row.SizeID,
                "sizeName": row.SizeName,
                "isActive": row.IsActive,
                "createdAt": row.CreatedAt,
                "updatedAt": row.UpdatedAt,
            }
            for row in result
        ]

    @staticmethod
    def size_read_by_id(db: Session, size_id: int):
        query = text("EXEC Sizes_ReadByID :SizeID")
        result = db.execute(query, {"SizeID": size_id}).mappings().fetchone()

        if not result:
            return None

        return {
            "SizeID": result["SizeID"],
            "SizeName": result["SizeName"],
            "IsActive": result["IsActive"],
            "CreatedAt": result["CreatedAt"],
            "UpdatedAt": result["UpdatedAt"],
        }

    @staticmethod
    def size_create(db: Session, size_data: SizeCreateSchema):
        query = text("EXEC Sizes_Create :sizeName, :isActive")
        db.execute(
            query,
            {
                "sizeName": size_data.SizeName,
                "isActive": size_data.IsActive,
            },
        )
        db.commit()

    @staticmethod
    def size_update(db: Session, size_data: SizeUpdateSchema):
        try:
            query = text("EXEC Sizes_Update :sizeID, :sizeName, :isActive")
            db.execute(
                query,
                {
                    "sizeID": size_data.SizeID,
                    "sizeName": size_data.SizeName,
                    "isActive": size_data.IsActive,
                },
            )
            db.commit()
        except Exception as e:
            db.rollback()
            raise ValueError(f"Failed to update size: {str(e)}")
        
    @staticmethod
    def size_delete(db: Session, size_id: int):
        try:
            query = text("EXEC Sizes_Delete :SizeID")
            db.execute(query, {"SizeID": size_id})
            db.commit()
        except Exception as e:
            db.rollback()
            raise ValueError(f"Failed to delete size: {str(e)}")