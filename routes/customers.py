from fastapi import APIRouter, HTTPException

from dependencies import get_customer_controller

router = APIRouter()


@router.get("/customer-orders_and_status")
def get_customer_orders_and_status(state: str, status: str):
    conn, customer_controller = get_customer_controller()
    try:
        customer_orders = customer_controller.get_customer_orders_And_status(
            state, status
        )
        return {"customer_orders": customer_orders}
    finally:
        conn.close()


@router.get("/customer-ids")
def get_customer_ids():
    conn, customer_controller = get_customer_controller()
    try:
        customer_ids = customer_controller.get_customer_ids()
        return {"customer_ids": customer_ids}
    finally:
        conn.close()


@router.get("/customers-total")
def get_total_customers():
    conn, customer_controller = get_customer_controller()
    try:
        total_customers = customer_controller.get_total_customers()
        return {"total_customers": total_customers}
    finally:
        conn.close()


@router.get("/customer-states")
def get_customer_states():
    conn, customer_controller = get_customer_controller()
    try:
        customer_states = customer_controller.get_customer_states()
        return {"customer_states": customer_states}
    finally:
        conn.close()

@router.get("/customer-ids_where_city")
def get_customer_ids_where_city(customer_city: str):
    conn, customer_controller = get_customer_controller()
    try:
        customer_ids = customer_controller.get_customer_ids_where_city(customer_city)
        return {"customer_ids": customer_ids}
    finally:
        conn.close()

@router.get("/customer-cities")
def get_customer_cities():
    conn, customer_controller = get_customer_controller()
    try:
        customer_cities = customer_controller.get_customer_cities()
        return {"customer_cities": customer_cities}
    finally:
        conn.close()


@router.delete("/delete-customer/{customer_id}")
def delete_customer(customer_id: str):
    conn, customer_controller = get_customer_controller()
    try:
        result = customer_controller.delete_customer(customer_id)
        return result
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
    finally:
        conn.close()

@router.put("/update-customer/{customer_id}")
def update_customer(customer_id: str, new_customer_id: str):
    conn, customer_controller = get_customer_controller()
    try:
        result = customer_controller.update_customer(customer_id, new_customer_id)
        return result
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
    finally:
        conn.close()
