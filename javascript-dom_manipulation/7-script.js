fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        const moviesList = document.querySelector('#list_movies');
        data.results.forEach(movie => {
            let listItem = document.createElement('li');
            listItem.textContent = movie.title;
            moviesList.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error fetching data:', error));
