# FastAPI E-Commerce SQL

Backend learning project built with FastAPI and SQLite.

## Overview

This project demonstrates a small e-commerce backend with REST API endpoints for customers, orders, and payments. It also includes simple HTML pages for testing data in the browser.

## Features

- Read customer, order, and payment data from SQLite
- Filter customers by city
- Filter orders by status and customer state
- Show payment statistics
- Create a new customer together with a new order
- Delete a customer by `customer_id`
- Test pages built with Jinja2 and JavaScript

## Tech Stack

- Python
- FastAPI
- SQLite
- Jinja2
- JavaScript

## Project Structure

```text
app.py
controller.py
dependencies.py
model.py
service.py
routes/
templates/
static/
```

## Run Locally

1. Create and activate a virtual environment.
2. Install the dependencies you use for FastAPI.
3. Start the app:

```bash
uvicorn app:app --reload
```

4. Open in the browser:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/customer-pages`
- `http://127.0.0.1:8000/payments-page`
- `http://127.0.0.1:8000/docs`

## Example API Endpoints

- `GET /customer-ids`
- `GET /customer-cities`
- `GET /customer-orders_and_status`
- `GET /order-statuses`
- `GET /order-ids-by-status`
- `GET /payments`
- `POST /customer-orders`
- `DELETE /delete-customer/{customer_id}`

## Example POST Request

```json
{
  "customer_id": "cust_1002",
  "customer_unique_id": "unique_1002",
  "customer_zip_code_prefix": 10115,
  "customer_city": "Berlin",
  "customer_state": "BE",
  "order_id": "order_1002",
  "order_status": "processing",
  "order_purchase_timestamp": "2026-08-15 17:00:00",
  "order_estimated_delivery_date": "2026-08-20 18:00:00"
}
```

## Learning Goal

This project was built to practice:

- REST API development with FastAPI
- SQL queries and joins
- CRUD operations
- separating code into routes, controller, service, and model layers

## Next Improvements

- Add automated tests
- Improve validation and error handling
- Clean up route naming
- Add update endpoints
- Improve frontend styling for the test pages
