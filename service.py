from datetime import datetime

from model import Customer, Order, OrderItem, OrderItemWithPrice, Payments

class CustomerService:
    def __init__(self, conn):
        self.conn = conn


    # Update customer from customer_id)
    def update_customer(self, customer_id, new_customer_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE customers SET customer_id = ? WHERE customer_id = ?",
            (new_customer_id, customer_id),
        )
        if cursor.rowcount == 0:
            raise ValueError(f"Customer with ID {customer_id} was not found.")
        self.conn.commit()
        return {"message": f"Customer ID updated from {customer_id} to {new_customer_id}."}


    
    def delete_customer(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
        if cursor.rowcount == 0:
            raise ValueError(f"Customer with ID {customer_id} was not found.")
        self.conn.commit()
        return {"message": f"Customer with ID {customer_id} deleted successfully."}

    def create_customer_order(self, customer_order_data):
        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT 1 FROM customers WHERE customer_id = ?",
            (customer_order_data.customer_id,),
        )
        if cursor.fetchone():
            raise ValueError("Customer ID exists already.")

        cursor.execute(
            "SELECT 1 FROM orders WHERE order_id = ?",
            (customer_order_data.order_id,),
        )
        if cursor.fetchone():
            raise ValueError("Order ID exists already.")

        purchase_timestamp = (
            customer_order_data.order_purchase_timestamp
            or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        cursor.execute(
            """
            INSERT INTO customers (
                customer_id,
                customer_unique_id,
                customer_zip_code_prefix,
                customer_city,
                customer_state
            ) VALUES (?, ?, ?, ?, ?)
            """,
            (
                customer_order_data.customer_id,
                customer_order_data.customer_unique_id,
                customer_order_data.customer_zip_code_prefix,
                customer_order_data.customer_city,
                customer_order_data.customer_state,
            ),
        )

        cursor.execute(
            """
            INSERT INTO orders (
                order_id,
                customer_id,
                order_status,
                order_purchase_timestamp,
                order_approved_at,
                order_delivered_carrier_date,
                order_delivered_customer_date,
                order_estimated_delivery_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                customer_order_data.order_id,
                customer_order_data.customer_id,
                customer_order_data.order_status,
                purchase_timestamp,
                customer_order_data.order_approved_at,
                customer_order_data.order_delivered_carrier_date,
                customer_order_data.order_delivered_customer_date,
                customer_order_data.order_estimated_delivery_date,
            ),
        )

        self.conn.commit()
        return {
            "message": "Customer and order created successfully.",
            "customer_id": customer_order_data.customer_id,
            "order_id": customer_order_data.order_id,
        }

    def get_customer(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT customer_id," \
        " customer_city, " \
        "customer_state " \
        "FROM customers LIMIT 10")
        rows = cursor.fetchall()
        customers = []
        for row in rows:
            customer = Customer(row[0], row[1], row[2])
            customers.append(customer)
        return customers

    # customer_id methode filtered with customer_city
    def get_customer_cities(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT DISTINCT customer_city FROM customers WHERE customer_city IS NOT NULL ORDER BY customer_city "
        )
        rows = cursor.fetchall()
        customer_cities = []
        for row in rows:
            customer_city = row[0]
            customer_cities.append(customer_city)
        return customer_cities
    def get_customer_ids_where_city(self, customer_city):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT " \
            "customers.customer_id, " \
            "customers.customer_city, " \
            "customers.customer_state " \
            "FROM customers WHERE customer_city = ? AND customer_id IS NOT NULL LIMIT 15",
            (customer_city,),
        )
        rows = cursor.fetchall()
        customer_ids = []
        for row in rows:
            customer_wher_city= Customer(row[0], row[1], row[2])
            customer_ids.append(customer_wher_city)
        return customer_ids

    def get_customer_ids(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT customer_id FROM customers WHERE customer_id IS NOT NULL LIMIT 15",
            )
        
        rows = cursor.fetchall()
        customer_ids = []
        for row in rows:
            customer_id = row[0]
            customer_ids.append(customer_id)
        return customer_ids

    def get_customer_states(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT DISTINCT customer_state
            FROM customers
            WHERE customer_state IS NOT NULL
            ORDER BY customer_state
        """)
        rows = cursor.fetchall()
        return [row[0] for row in rows]

    def get_order_statuses(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT DISTINCT order_status
            FROM orders
            WHERE order_status IS NOT NULL
            ORDER BY order_status
        """)
        rows = cursor.fetchall()
        return [row[0] for row in rows]


#  get customer_orders nach query state
    def get_customer_orders_And_status(self, state, status):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT
                customers.customer_id,
                customers.customer_state,
                orders.order_id,
                orders.order_status
            FROM customers
            JOIN orders
                ON customers.customer_id = orders.customer_id
            WHERE customers.customer_state = ? AND orders.order_status = ?
            LIMIT 5

            """, (state, status))
        rows = cursor.fetchall()
        state_order_and_status = []
        for row in rows:
            stateorder = {
                "customer_id": row[0],
                "customer_state": row[1],
                "order_id": row[2],
                "order_status": row[3]
            }
            state_order_and_status.append(stateorder)
        return state_order_and_status

###########################################################



    # zeige alle Bestellung die nicht als delivered markiert sind
    def get_undelivered_orders(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT
            customers.customer_id,
            customers.customer_state,
            orders.order_id,
            orders.order_status
        FROM customers
        JOIN orders
            ON customers.customer_id = orders.customer_id
        WHERE orders.order_status != 'delivered'
       
        """)
        rows = cursor.fetchall()

        undelivered_orders = []
        for row in rows:
            undelivered_order = {
                "customer_id": row[0],
                "customer_state": row[1],
                "order_id": row[2],
                "order_status": row[3]
            }
            undelivered_orders.append(undelivered_order)
        return undelivered_orders



    # eine zweite methode für customer order 
    def get_customer_orders_v2(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT
            customer_id,
            order_id,
            order_status
        FROM orders
        LIMIT 5
        """)
        rows = cursor.fetchall()

        customer_orders = []
        for row in rows:
            customer_order = {
                "customer_id": row[0],
                "order_id": row[1],
                "order_status": row[2]
            }
            customer_orders.append(customer_order)
        return customer_orders




    # join order_itesm with products to get product details for each order item

    def get_order_items_with_product_details(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT
            order_items.order_id,
            order_items.product_id,
            order_items.seller_id,
            order_items.shipping_limit_date,
            order_items.price,
            order_items.freight_value,
            products.product_category_name,
            products.product_name_lenght    
        FROM order_items
        JOIN products
            ON order_items.product_id = products.product_id
        LIMIT 5

        """)
        rows = cursor.fetchall()

        order_items_with_product_details = []
        # get objects from rows and append to list
        for row in rows:
            order_item_with_product_detail = OrderItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            order_items_with_product_details.append(order_item_with_product_detail)

        return order_items_with_product_details


    # join order_items with products with orders 

    def get_order_items_with_product_details_and_orders(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT
            order_items.order_id,
            order_items.product_id,
            order_items.seller_id,
            order_items.shipping_limit_date,
            order_items.price,
            order_items.freight_value,
            products.product_category_name,
            orders.order_status
        FROM order_items
        JOIN products
            ON order_items.product_id = products.product_id
        JOIN orders
            ON order_items.order_id = orders.order_id
        LIMIT 5

        """)
        rows = cursor.fetchall()

        order_items_with_product_details_and_orders = []
        for row in rows:
            order_item_with_product_detail_and_order = OrderItem(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
            )
            
            order_items_with_product_details_and_orders.append(order_item_with_product_detail_and_order)
        return order_items_with_product_details_and_orders



    # parametrisierte methode für orders

    def get_orders_by_status(self, status):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT order_id, customer_id, order_status
            FROM orders
            WHERE order_status = ?
            LIMIT 5
        """, (status,))

        rows = cursor.fetchall()

        orders = []
        for row in rows:
            order = Order(row[0], row[1], row[2])
            orders.append(order)
        return orders



# nach dem erstellen der service klasse, kann man die methode get
# customer() aufrufen, um die Kunden aus der Datenbank abzurufen.

    def get_order_items(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT order_id, product_id, seller_id, shipping_limit_date, price, freight_value
        FROM order_items
        LIMIT 5
    """)
        rows = cursor.fetchall()
        order_items = []
        for row in rows:
            order_item = OrderItem(row[0], row[1], row[2], row[3], row[4], row[5])
            order_items.append(order_item)
        return order_items


    
    def get_order_item_with_price(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT order_id, price
        FROM order_items
        LIMIT 5
    """)
        rows = cursor.fetchall()
        order_items_with_price = []
        for row in rows:
            order_item_with_price = OrderItemWithPrice(row[0], row[1])
            order_items_with_price.append(order_item_with_price)
        return order_items_with_price



    # Anzahl der Orders pro state anzeigen###

    def get_order_count_by_state(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT customers.customer_state, COUNT(orders.order_id) AS order_count
            FROM customers
            JOIN orders ON customers.customer_id = orders.customer_id
            GROUP BY customers.customer_state
            ORDER BY order_count DESC LIMIT 5
        """)
        rows = cursor.fetchall()
        order_count_by_state = []
        for row in rows:
            state_order_count = {
                "customer_state": row[0],
                "order_count": row[1]
            }
            order_count_by_state.append(state_order_count)
        return order_count_by_state

    # Payments 

    def get_payments(self, min_payment_value, max_payment_value):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT order_id, payment_sequential, payment_type, payment_installments, payment_value
            FROM order_payments
            WHERE payment_value BETWEEN ? AND ?
            LIMIT 15
        """, (min_payment_value, max_payment_value))
        rows = cursor.fetchall()
        payments = []
        for row in rows:
            payment = Payments(row[0], row[1], row[2], row[3], row[4])
            payments.append(payment)
        return payments

    # orderId by Order status
    def get_order_ids_by_status(self, status):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT 
            orders.order_id,
            orders.customer_id,
            orders.order_status

            FROM orders
            WHERE order_status = ?
            LIMIT 15
        """, (status,))
        rows = cursor.fetchall()
        order_by_status = []
        for row in rows:
            ordered_by_status = Order(row[0], row[1], row[2])
            order_by_status.append(ordered_by_status)
        return order_by_status

    # payement-states min max average
    def get_payment_stats(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT 
                MIN(payment_value) AS min_payment,
                MAX(payment_value) AS max_payment,
                AVG(payment_value) AS avg_payment
            FROM order_payments
        """)
        row = cursor.fetchone()
        payment_stats = {
            "min_payment": row[0],
            "max_payment": row[1],
            "avg_payment": row[2]
        }
        return payment_stats
