// etches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  const res = data.results;
  const mlist = $('ul#list_movies');
  for (let i = 0; i < res.length; i++) {
    mlist.append(`<lis>${res[i].title}</li>`);
  }
});
