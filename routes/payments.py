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
    