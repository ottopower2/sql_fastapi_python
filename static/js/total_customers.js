async function loadTotalCustomers() {
  const resultElement = document.getElementById('total-customers-result');
  resultElement.textContent = 'Loading...';

  try {
    const response = await fetch('/customers-total');
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || 'Could not load total customers.');
    }

    resultElement.textContent = `Total customers: ${data.total_customers}`;
  } catch (error) {
    resultElement.textContent = `Error: ${error.message}`;
  }
}
