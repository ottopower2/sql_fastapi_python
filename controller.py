class CustomerController:
    def __init__(self, customer_service):
        self.customer_service = customer_service

    def get_customers(self):
        return self.customer_service.get_customer()
    
    def get_customer_ids(self):
        return self.customer_service.get_customer_ids()

    def get_total_customers(self):
        return self.customer_service.get_total_customers()

    def get_customer_states(self):
        return self.customer_service.get_customer_states()

    def get_order_statuses(self):
        return self.customer_service.get_order_statuses()

    def get_customer_orders_And_status(self, state, status):
        return self.customer_service.get_customer_orders_And_status(state, status)

    def get_customer_orders(self, state):
        return self.customer_service.get_customer_orders(state)

    def get_undelivered_orders(self):
        return self.customer_service.get_undelivered_orders()

    def get_customer_orders_v2(self):
        return self.customer_service.get_customer_orders_v2()

    def get_order_items_with_product_details(self):
        return self.customer_service.get_order_items_with_product_details()

    def get_order_items_with_product_details_and_orders(self):
        return self.customer_service.get_order_items_with_product_details_and_orders()


    def get_orders_by_status(self, status):
        return self.customer_service.get_orders_by_status(status) 


    def get_order_items(self):
        return self.customer_service.get_order_items()



    def get_expensive_order_items(self, min_price):
            order_items = self.get_order_items()

            expensive_items = []
            for item in order_items:
                if item.price >= min_price:
                    expensive_items.append(item)

            return expensive_items


    def get_products_with_price_above(self, min_price):
        return self.customer_service.get_products_with_price_above(min_price)

    def get_order_item_with_price(self):
        return self.customer_service.get_order_item_with_price()


    def get_order_count_by_state(self):
        return self.customer_service.get_order_count_by_state()

    def get_payments(self, min_payment_value, max_payment_value):
        return self.customer_service.get_payments(
            min_payment_value, max_payment_value
        )

    def get_customer_ids_where_city(self, customer_city):
     return self.customer_service.get_customer_ids_where_city(customer_city)

    def get_customer_cities(self):
        return self.customer_service.get_customer_cities()



    def get_order_ids_by_status(self, status):
        return self.customer_service.get_order_ids_by_status(status)


    def get_payment_stats(self):
        return self.customer_service.get_payment_stats()

    def create_customer_order(self, customer_order_data):
        return self.customer_service.create_customer_order(customer_order_data)

    def delete_customer(self, customer_id):
        return self.customer_service.delete_customer(customer_id)

    def update_customer(self, customer_id, new_customer_id):
        return self.customer_service.update_customer(customer_id, new_customer_id)
