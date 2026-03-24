window.addEventListener('load', () => {
  const greeting = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      greeting.textContent = data.hello;
    });
});
