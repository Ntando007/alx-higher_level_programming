$.get('https://swapi.co/api/films/?format=json', (data) => {
    $.each(data.results, (i, movie) => {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
});