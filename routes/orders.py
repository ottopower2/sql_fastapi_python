from fastapi import APIRouter, HTTPException

from dependencies import get_customer_controller
from model import CustomerOrderCreate

router = APIRouter()

@router.get("/order-statuses")
def get_order_statuses():
    conn, customer_controller = get_customer_controller()
    try:
        order_statuses = customer_controller.get_order_statuses()
        return {"order_statuses": order_statuses}
    finally:
        conn.close()


@router.post("/customer-orders")
def create_customer_order(customer_order: CustomerOrderCreate):
    conn, customer_controller = get_customer_controller()
    try:
        return customer_controller.create_customer_order(customer_order)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    finally:
        conn.close()


@router.get("/order-item-with-price")
def get_order_item_with_price():
    conn, customer_controller = get_customer_controller()
    try:
        order_item_with_price = customer_controller.get_order_item_with_price()
        return {"order_item_with_price": order_item_with_price}
    finally:
        conn.close()


@router.get("/order_count_by_state")
def get_order_count_by_state():
    conn, customer_controller = get_customer_controller()
    try:
        order_count_by_state = customer_controller.get_order_count_by_state()
        return {"order_count_by_state": order_count_by_state}
    finally:
        conn.close()


@router.get("/order-ids-by-status")
def get_order_ids_by_status(status: str):
    conn, customer_controller = get_customer_controller()
    try:
        order_ids_by_status = customer_controller.get_order_ids_by_status(status)
        return {"order_ids_by_status": order_ids_by_status}
    finally:
        conn.close()
