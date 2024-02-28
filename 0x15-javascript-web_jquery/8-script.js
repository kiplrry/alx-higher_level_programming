$(function () {
  $.ajax();
  $.get({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      console.log(data);
      $.each(data.results, (ind, val) => {
        $('UL#list_movies').append(`<LI>${val.title}</LI>`);
      });
    },
    dataType: 'json'
  });
});
