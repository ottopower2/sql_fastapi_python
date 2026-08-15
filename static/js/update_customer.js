// Update customer ID with new Customer ID
function updateCustomerid() {
  const customerId = document.getElementById('update_customer_id').value;
  const newCustomerId = document.getElementById('new_customer_id').value;
  fetch(
    `/update-customer/${encodeURIComponent(customerId)}?new_customer_id=${encodeURIComponent(newCustomerId)}`,
    {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ new_customer_id: newCustomerId }),
    },
  )
    .then((response) => response.json())
    .then((data) => {
      document.getElementById('update-customer-result').textContent =
        JSON.stringify(data);
    })
    .catch((error) => {
      document.getElementById('update-customer-result').textContent =
        `Error: ${error}`;
    });
}
