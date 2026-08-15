// update customer.js
function UpdateCustomerId() {
  const customerId = document.getElementById('customer_id').value;
  const url = `/update-customer/${customerId}`;
  fetch(url, {
    method: 'PUT',
  })
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
