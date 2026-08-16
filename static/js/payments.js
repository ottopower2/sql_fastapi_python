function loadPayments() {
  const minPaymentValue = document.getElementById('min_payment_value').value;
  const maxPaymentValue = document.getElementById('max_payment_value').value;
  const list = document.getElementById('payments-list');

  if (minPaymentValue === '' || maxPaymentValue === '') {
    list.innerHTML = '<li>Please enter both values.</li>';
    return;
  }

  fetch(
    '/payments?min_payment_value=' +
      minPaymentValue +
      '&max_payment_value=' +
      maxPaymentValue,
  )
    .then((response) => response.json())
    .then((data) => {
      list.innerHTML = '';

      data.payments.forEach((payment) => {
        const li = document.createElement('li');
        li.textContent =
          'Order ID: ' +
          payment.order_id +
          ', Payment Sequential: ' +
          payment.payment_sequential +
          ', Payment Type: ' +
          payment.payment_type +
          ', Payment Installments: ' +
          payment.payment_installments +
          ', Payment Value: ' +
          payment.payment_value;
        list.appendChild(li);
      });

      if (data.payments.length === 0) {
        list.innerHTML = '<li>No payments found.</li>';
      }
    });
}

function loadPaymentStats() {
  fetch('/payment-stats')
    .then((response) => response.json())
    .then((data) => {
      document.getElementById('min-payment-value').textContent =
        data.payment_stats.min_payment.toFixed(2);

      document.getElementById('max-payment-value').textContent =
        data.payment_stats.max_payment.toFixed(2);

      document.getElementById('avg-payment-value').textContent =
        data.payment_stats.avg_payment.toFixed(2);
    });
}

function loadCities() {
  fetch('/selectcity')
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      const citySelect = document.getElementById('city-select');
      const cities = data.customer_cities || data.cities || [];
      citySelect.innerHTML = '<option value="">Choose a city</option>';
      cities.forEach((city) => {
        const option = document.createElement('option');
        option.value = city;
        option.textContent = city;
        citySelect.appendChild(option);
      });
    })
    .catch((error) => {
      console.error('Error loading cities:', error);
    });
}

function loadTotalPaymentsByCity() {
  const city = document.getElementById('city-select').value;
  const resultElement = document.getElementById('total-payments-by-city');

  if (!city) {
    resultElement.textContent = 'Please choose a city first.';
    return;
  }

  fetch(`/total_payments_by_city?city=${encodeURIComponent(city)}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      if (data.total_payments === null) {
        resultElement.textContent = 'No payments found for this city.';
        return;
      }

      resultElement.textContent = Number(data.total_payments).toFixed(2);
    })
    .catch((error) => {
      resultElement.textContent = 'Could not load total payments.';
      console.error('Error loading total payments by city:', error);
    });
}

document.addEventListener('DOMContentLoaded', loadCities);

function loadTotalRevenueBySeller() {
  const sellerId = document.getElementById('seller-id-input').value;
  const resultElement = document.getElementById('total-revenue-by-seller');

  if (!sellerId) {
    resultElement.textContent = 'Please enter a seller ID first.';
    return;
  }

  fetch(`/total_revenue_by_seller?seller_id=${encodeURIComponent(sellerId)}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      if (data.total_revenue === null) {
        resultElement.textContent = 'No revenue found for this seller.';
        return;
      }

      resultElement.textContent = Number(data.total_revenue).toFixed(2);
    })
    .catch((error) => {
      resultElement.textContent = 'Could not load total revenue.';
      console.error('Error loading total revenue by seller:', error);
    });
}
