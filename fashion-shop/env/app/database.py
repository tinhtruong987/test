from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from sqlalchemy.sql import text

# Load environment variables
load_dotenv(dotenv_path="c:/Users/tinhk/Desktop/BE/fashion-shop/env/.env")

# Fetch DATABASE_URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"DATABASE_URL: {DATABASE_URL}")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model
Base = declarative_base()

def init_db():
    from app.models.product_model import Product
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def execute_stored_procedure(procedure_name: str, params: dict = None):
    """
    Execute a stored procedure with optional parameters.
    :param procedure_name: Name of the stored procedure.
    :param params: Dictionary of parameters to pass to the procedure.
    :return: Result of the procedure execution.
    """
    with engine.connect() as connection:
        if params:
            query = text(f"EXEC {procedure_name} :{', :'.join(params.keys())}")
            result = connection.execute(query, **params)
        else:
            query = text(f"EXEC {procedure_name}")
            result = connection.execute(query)
        return result.fetchall()