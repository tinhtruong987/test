from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.product_controller import router as ProductRouter
from app.controllers.order_controller import router as OrderRouter
from app.controllers.customer_controller import router as CustomerRouter
from app.controllers.staff_controller import router as StaffRouter
from app.controllers.auth_controller import router as AuthRouter
from app.controllers.category_controller import router as CategoryRouter
from app.database import init_db

# Initialize FastAPI app
app = FastAPI()

# Initialize the database
init_db()

# Include product controller routes
app.include_router(ProductRouter)

# Include order controller routes
app.include_router(OrderRouter)

# Include customer controller routes
app.include_router(CustomerRouter)
# Include customer controller routes
app.include_router(StaffRouter)

# Include customer controller routes
app.include_router(AuthRouter)

# Include customer controller routes
app.include_router(CategoryRouter)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Thay đổi nếu frontend chạy ở domain khác
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Fashion Shop API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)