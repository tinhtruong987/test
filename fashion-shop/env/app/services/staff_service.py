from sqlalchemy import text
from sqlalchemy.orm import Session
from app.models.staff_model import Staff
from app.views.staff_view import StaffCreateSchema, StaffUpdateSchema


class staffService:
    @staticmethod
    def staff_get_all(db: Session):
        query = text("EXEC Staff_GetAll")
        result = db.execute(query).fetchall()
        return [
            {
                "StaffID": row.StaffID,
                "UserAccountID": row.UserAccountID,
                "Name": row.Name,
                "Position": row.Position,
                "IsActive": row.IsActive,
                "CreatedAt": row.CreatedAt,
                "UpdatedAt": row.UpdatedAt,
            }
            for row in result
        ]

    @staticmethod
    def staff_read_by_id(db: Session, staff_id: int):
        query = text("EXEC Staff_ReadByID :StaffID")
        result = db.execute(query, {"StaffID": staff_id}).mappings().fetchone()

        if not result:
            return None

        return {
            "staffID": result["StaffID"],
            "userAccountID": result["UserAccountID"],
            "name": result["Name"],
            "position": result["Position"],
            "isActive": result["IsActive"],
            "createdAt": result["CreatedAt"],
            "updatedAt": result["UpdatedAt"],
        }


    @staticmethod
    def staff_create(db: Session, staff_data: StaffCreateSchema):
        query = text(
            "EXEC staff_Create :userAccountID, :Name, :Position"
        )
        db.execute(
            query,
            {
                "userAccountID": staff_data.userAccountID,
                "Name": staff_data.Name,
                "Position": staff_data.Position,
            },
        )
        db.commit()


    @staticmethod
    def staff_update(db: Session, staff_data: StaffUpdateSchema):
        try:
            query = text(
                "EXEC staff_Update :staffID, :userAccountID, :Name, :Position, :IsActive"
            )
            db.execute(
                query,
                {
                    "staffID": staff_data.StaffID,
                    "userAccountID": staff_data.userAccountID,
                    "Name": staff_data.Name,
                    "Position": staff_data.Position,
                    "IsActive": staff_data.IsActive,
                },
            )
            db.commit()
        except Exception as e:
            db.rollback()
            raise ValueError(f"Failed to update staff: {str(e)}")

    @staticmethod
    def staff_delete(db: Session, staff_id: int):
        try:
            query = text("EXEC Staff_Delete :StaffID")
            db.execute(query, {"StaffID": staff_id})
            db.commit()
        except Exception as e:
            db.rollback()
            raise ValueError(f"Failed to delete staff: {str(e)}")
