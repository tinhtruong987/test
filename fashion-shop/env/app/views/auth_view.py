# app/views/auth_view.py

from pydantic import BaseModel

class AuthLoginSchema(BaseModel):
    username: str
    password: str