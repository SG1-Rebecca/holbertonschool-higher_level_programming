const request = new Request('https://swapi-api.hbtn.io/api/films/?');
const listMovies = document.getElementById('list_movies');

window.fetch(request)
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then((data) => {
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      listMovies.append(li);
    });
  })
  .catch((error) => {
    console.error('Fetch error: ', error);
  });
