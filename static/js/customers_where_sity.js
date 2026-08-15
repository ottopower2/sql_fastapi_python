function loadCustomerCities() {
  fetch('/customer-cities')
    .then((response) => response.json())
    .then((data) => {
      const select = document.getElementById('city-select');
      select.innerHTML = '<option value="">Choose a city</option>';

      data.customer_cities.forEach((city) => {
        const option = document.createElement('option');
        option.value = city;
        option.textContent = city;
        select.appendChild(option);
      });
    });
}
// Load customer cities on page load
document.addEventListener('DOMContentLoaded', () => {
  loadCustomerCities();
});

// Load customer cities on page load
function loadCustomerIdsWhereCity() {
  const city = document.getElementById('city-select').value;
  if (city === '') {
    alert('Please select a city first.');
    return;
  }

  fetch('/customer-ids_where_city?customer_city=' + city)
    .then((response) => response.json())
    .then((data) => {
      const list = document.getElementById('customer-ids-by-city-list');
      list.innerHTML = '';

      data.customer_ids.forEach((item) => {
        const li = document.createElement('li');
        li.textContent =
          'Customer ID: ' +
          item.customer_id +
          ', City: ' +
          item.customer_city +
          ', State: ' +
          item.customer_state;
        list.appendChild(li);
      });
    });
}
