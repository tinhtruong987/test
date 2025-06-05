from sqlalchemy import text
from sqlalchemy.orm import Session
from app.models.user_model import UserAccount
from app.views.user_view import (
    UserAccountCreateSchema,
    UserAccountUpdateSchema,
)

class UserAccountService:
    @staticmethod
    def user_get_all(db: Session):
        query = text("EXEC UserAccount_GetAll")
        result = db.execute(query).fetchall()
        return [
            {
                "UserAccountID": row.UserAccountID,
                "Username": row.Username,
                "PasswordHash": row.PasswordHash,
                "Email": row.Email,
                "Role": row.Role,
                "IsActive": row.IsActive,
                "CreatedAt": row.CreatedAt,
                "UpdatedAt": row.UpdatedAt,
            }
            for row in result
        ]

    @staticmethod
    def user_read_by_id(db: Session, user_id: int):
        query = text("EXEC UserAccount_ReadByID :UserAccountID")
        result = db.execute(query, {"UserAccountID": user_id})
        return result.fetchone()

    @staticmethod
    def user_create(db: Session, user_data: UserAccountCreateSchema):
        query = text("""
            EXEC UserAccount_Create 
                :Username, :PasswordHash, :Email, :Role, :IsActive, :CreatedAt, :UpdatedAt
        """)
        db.execute(query, {
            "Username": user_data.Username,
            "PasswordHash": user_data.PasswordHash,
            "Email": user_data.Email,
            "Role": user_data.Role,
            "IsActive": user_data.IsActive,
            "CreatedAt": user_data.CreatedAt,
            "UpdatedAt": user_data.UpdatedAt
        })
        db.commit()

    @staticmethod
    def user_update(db: Session, user_data: UserAccountUpdateSchema):
        try:
            query = text("""
                EXEC UserAccount_Update 
                    :UserAccountID, :Username, :PasswordHash, :Email, :Role, :IsActive, :CreatedAt, :UpdatedAt
            """)
            db.execute(query, {
                "UserAccountID": user_data.UserAccountID,
                "Username": user_data.Username,
                "PasswordHash": user_data.PasswordHash,
                "Email": user_data.Email,
                "Role": user_data.Role,
                "IsActive": user_data.IsActive,
                "CreatedAt": user_data.CreatedAt,
                "UpdatedAt": user_data.UpdatedAt
            })
            db.commit()
        except Exception as e:
            db.rollback()
            raise ValueError(f"Failed to update user account: {str(e)}")
