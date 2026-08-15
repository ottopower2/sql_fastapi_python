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
