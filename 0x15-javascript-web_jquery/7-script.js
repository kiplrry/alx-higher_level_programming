$(function () {
  $.ajax();
  $.get({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?',
    success: function (data) {
      $('DIV#character').text(data.name);
    },
    dataType: 'json'
  });
});
