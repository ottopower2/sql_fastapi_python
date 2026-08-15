import sqlite3

from controller import CustomerController
from service import CustomerService


def get_customer_controller():
    conn = sqlite3.connect("olist.sqlite")
    customer_service = CustomerService(conn)
    customer_controller = CustomerController(customer_service)
    return conn, customer_controller
