const header = document.getElementById('character');
const request = new Request('https://swapi-api.hbtn.io/api/people/5/?format=json');

window.fetch(request)
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then((data) => {
    header.innerHTML = data.name;
  })
  .catch((error) => {
    console.error('Fetch error: ', error);
  });
