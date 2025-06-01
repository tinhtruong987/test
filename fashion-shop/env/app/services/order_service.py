from app.database import execute_stored_procedure

class OrderService:
    @staticmethod
    async def create_order(order_data: dict):
        return await execute_stored_procedure("Order_Create", order_data)

    @staticmethod
    async def get_all_orders():
        result = execute_stored_procedure("Order_GetAll")
        return result

    @staticmethod
    async def get_order_by_id(order_id: int):
        return await execute_stored_procedure("Order_GetByID", {"OrderID": order_id})

    @staticmethod
    async def update_order(order_id: int, order_data: dict):
        order_data["OrderID"] = order_id
        return await execute_stored_procedure("Order_Update", order_data)

    @staticmethod
    async def delete_order(order_id: int):
        return await execute_stored_procedure("Order_Delete", {"OrderID": order_id})

    @staticmethod
    async def add_order_item(order_item_data: dict):
        return await execute_stored_procedure("OrderItems_Add", order_item_data)

    @staticmethod
    async def get_order_items_by_order_id(order_id: int):
        return await execute_stored_procedure("OrderItems_GetByOrderID", {"OrderID": order_id})

    @staticmethod
    async def delete_order_item(order_item_id: int):
        return await execute_stored_procedure("OrderItems_DeleteByID", {"OrderItemID": order_item_id})

    @staticmethod
    async def delete_order_items_by_order_id(order_id: int):
        return await execute_stored_procedure("OrderItems_DeleteByOrderID", {"OrderID": order_id})
