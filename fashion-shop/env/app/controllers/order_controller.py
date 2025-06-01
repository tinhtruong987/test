from fastapi import APIRouter, HTTPException, Depends
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/Create")
async def create_order(order_data: dict):
    try:
        return await OrderService.create_order(order_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/GetAll")
async def get_all_orders():
    try:
        return await OrderService.get_all_orders()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/GetById/{order_id}")
async def get_order_by_id(order_id: int):
    try:
        return await OrderService.get_order_by_id(order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/Update/{order_id}")
async def update_order(order_id: int, order_data: dict):
    try:
        return await OrderService.update_order(order_id, order_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/Delete/{order_id}")
async def delete_order(order_id: int):
    try:
        return await OrderService.delete_order(order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/OrderItems/Add")
async def add_order_item(order_item_data: dict):
    try:
        return await OrderService.add_order_item(order_item_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/OrderItems/GetByOrderId/{order_id}")
async def get_order_items_by_order_id(order_id: int):
    try:
        return await OrderService.get_order_items_by_order_id(order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/OrderItems/DeleteById/{order_item_id}")
async def delete_order_item(order_item_id: int):
    try:
        return await OrderService.delete_order_item(order_item_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/OrderItems/DeleteByOrderId/{order_id}")
async def delete_order_items_by_order_id(order_id: int):
    try:
        return await OrderService.delete_order_items_by_order_id(order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
