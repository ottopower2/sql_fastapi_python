from fastapi import APIRouter

from dependencies import get_customer_controller

router = APIRouter()

@router.get("/payments")
def get_payments(min_payment_value: float, max_payment_value: float):
    conn, customer_controller = get_customer_controller()
    try:
        payments = customer_controller.get_payments(min_payment_value=min_payment_value, max_payment_value=max_payment_value)
        return {"payments": payments}
    finally:
        conn.close()


@router.get("/payment-stats")
def get_payment_stats():
    conn, customer_controller = get_customer_controller()
    try:
        payment_stats = customer_controller.get_payment_stats()
        return {"payment_stats": payment_stats}
    finally:
        conn.close()



@router.get("/total_payments_by_city")
def get_total_payments_by_city(city: str):
    conn, customer_controller = get_customer_controller()
    try:
        total_payments = customer_controller.get_total_payments_by_city(city)
        return {"total_payments": total_payments}
    finally:
        conn.close()

@router.get("/selectcity")
def get_selectcity():
    conn, customer_controller = get_customer_controller()
    try:
        customer_cities = customer_controller.get_customer_cities()
        return {"customer_cities": customer_cities}
    finally:
        conn.close()


@router.get("/total_revenue_by_seller")
def get_total_revenue_by_seller(seller_id: str):
    conn, customer_controller = get_customer_controller()
    try:
        total_revenue = customer_controller.get_total_revenue_by_seller(seller_id)
        return {"total_revenue": total_revenue}
    finally:
        conn.close()