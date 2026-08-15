# anhand olist.sqilte wird ein model erstellt 

from pydantic import BaseModel

class Customer:
    def __init__(self, customer_id, customer_city, customer_state):
        self.customer_id = customer_id
        self.customer_city = customer_city
        self.customer_state = customer_state


class Order:
    def __init__(self, order_id, customer_id, order_status):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_status = order_status



class OrderItem:
    def __init__(
        self,
        order_id,
        product_id,
        seller_id,
        shipping_limit_date,
        price,
        freight_value,
        product_category_name=None,
        order_status=None,
    ):
        self.order_id = order_id
        self.product_id = product_id
        self.seller_id = seller_id
        self.shipping_limit_date = shipping_limit_date
        self.price = price
        self.freight_value = freight_value
        self.product_category_name = product_category_name
        self.order_status = order_status

class OrderItemWithPrice:
    def __init__(self, order_id, price):
        self.order_id = order_id
        self.price = price


class Payments:
    def __init__(self, order_id, payment_sequential, payment_type, payment_installments, payment_value):
       
        self.order_id = order_id
        self.payment_sequential = payment_sequential
        self.payment_type = payment_type
        self.payment_installments = payment_installments
        self.payment_value = payment_value


class CustomerOrderCreate(BaseModel):
    customer_id: str
    customer_unique_id: str | None = None
    customer_zip_code_prefix: int | None = None
    customer_city: str
    customer_state: str
    order_id: str
    order_status: str
    order_purchase_timestamp: str | None = None
    order_approved_at: str | None = None
    order_delivered_carrier_date: str | None = None
    order_delivered_customer_date: str | None = None
    order_estimated_delivery_date: str | None = None
