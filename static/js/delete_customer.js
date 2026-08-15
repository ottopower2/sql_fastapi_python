// delet customer ID
function deleteCustomer() {
  const customerId = document.getElementById('delete_customer_id').value;
  const resultElement = document.getElementById('delete-customer-result');

  if (!customerId) {
    resultElement.textContent = 'Please enter a customer ID first.';
    return;
  }

  fetch(`/delete-customer/${encodeURIComponent(customerId)}`, {
    method: 'DELETE',
  })
    .then(async (response) => {
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.detail || 'Could not delete customer.');
      }
      return data;
    })
    .then((data) => {
      resultElement.textContent = data.message;
    })
    .catch((error) => {
      resultElement.textContent = `Error: ${error.message}`;
    });
}
