const customerOrderForm = document.getElementById('customer-order-form');
const customerOrderResult = document.getElementById('customer-order-result');

if (customerOrderForm) {
  customerOrderForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(customerOrderForm);
    const payload = {
      customer_id: formData.get('customer_id'),
      customer_unique_id: formData.get('customer_unique_id') || null,
      customer_zip_code_prefix: formData.get('customer_zip_code_prefix')
        ? Number(formData.get('customer_zip_code_prefix'))
        : null,
      customer_city: formData.get('customer_city'),
      customer_state: formData.get('customer_state'),
      order_id: formData.get('order_id'),
      order_status: formData.get('order_status'),
      order_purchase_timestamp:
        formData.get('order_purchase_timestamp') || null,
      order_estimated_delivery_date:
        formData.get('order_estimated_delivery_date') || null,
    };

    customerOrderResult.textContent = 'Saving...';

    try {
      const response = await fetch('/customer-orders', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (!response.ok) {
        customerOrderResult.textContent =
          'Error: ' + (data.detail || 'Could not save customer order.');
        return;
      }

      customerOrderResult.textContent =
        'Saved customer ' +
        data.customer_id +
        ' with order ' +
        data.order_id +
        '.';
      customerOrderForm.reset();
      document.getElementById('order_status').value = 'processing';
    } catch (error) {
      customerOrderResult.textContent =
        'Error: Request failed. Please try again.';
    }
  });
}
