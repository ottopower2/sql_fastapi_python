import sqlite3

import pytest

from service import CustomerService


@pytest.fixture
def service():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE customers (
            customer_id TEXT,
            customer_unique_id TEXT,
            customer_zip_code_prefix INTEGER,
            customer_city TEXT,
            customer_state TEXT
        )
        """
    )
    cursor.executemany(
        """
        INSERT INTO customers (
            customer_id,
            customer_unique_id,
            customer_zip_code_prefix,
            customer_city,
            customer_state
        ) VALUES (?, ?, ?, ?, ?)
        """,
        [
            ("cust_1", "unique_1", 10115, "berlin", "BE"),
            ("cust_2", "unique_2", 60311, "frankfurt", "HE"),
        ],
    )
    conn.commit()

    yield CustomerService(conn)

    conn.close()


def test_get_total_customers_returns_count(service):
    # Arrange is already done in the fixture above.

    # Act
    total_customers = service.get_total_customers()

    # Assert
    assert total_customers == 2


def test_delete_customer_removes_existing_customer(service):
    # Act
    result = service.delete_customer("cust_1")

    # Assert
    assert result["message"] == "Customer with ID cust_1 deleted successfully."
    assert service.get_total_customers() == 1


def test_delete_customer_raises_error_for_missing_customer(service):
    with pytest.raises(ValueError) as error:
        service.delete_customer("does_not_exist")

    assert str(error.value) == "Customer with ID does_not_exist was not found."
