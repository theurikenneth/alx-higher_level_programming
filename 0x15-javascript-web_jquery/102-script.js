$(document).ready(() => {
  $('input#btn_translate').click(() => {
    const lang = $('input#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/`, (data) => {
      $('div#hello').html(data.hello);
    });
  });
});
