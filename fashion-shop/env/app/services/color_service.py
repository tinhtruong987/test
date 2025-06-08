from sqlalchemy import text
from sqlalchemy.orm import Session
from app.views.color_view import ColorCreateSchema, ColorUpdateSchema

class ColorService:
    @staticmethod
    def color_get_all(db: Session):
        query = text("EXEC Colors_GetAll")
        result = db.execute(query).fetchall()
        return [
            {
                "ColorID": row.ColorID,
                "ColorName": row.ColorName,
                "IsActive": row.IsActive,
                "CreatedAt": row.CreatedAt,
                "UpdatedAt": row.UpdatedAt,
            }
            for row in result
        ]

    @staticmethod
    def color_read_by_id(db: Session, color_id: int):
        query = text("EXEC Colors_ReadByID :ColorID")
        result = db.execute(query, {"ColorID": color_id}).mappings().fetchone()
        if not result:
            return None
        return dict(result)

    @staticmethod
    def color_create(db: Session, color_data: ColorCreateSchema):
        query = text("EXEC Colors_Create :ColorName, :IsActive")
        db.execute(query, {
            "ColorName": color_data.ColorName,
            "IsActive": color_data.IsActive
        })
        db.commit()

    @staticmethod
    def color_update(db: Session, color_data: ColorUpdateSchema):
        try:
            query = text("EXEC Colors_Update :ColorID, :ColorName, :IsActive")
            db.execute(query, {
                "ColorID": color_data.ColorID,
                "ColorName": color_data.ColorName,
                "IsActive": color_data.IsActive
            })
            db.commit()
        except Exception as e:
            db.rollback()
            raise ValueError(f"Failed to update color: {str(e)}")

    @staticmethod
    def color_delete(db: Session, color_id: int):
        query = text("EXEC Colors_Delete :ColorID")
        db.execute(query, {"ColorID": color_id})
        db.commit()
