// adds, removes and clears LI elements from a list when the user clicks

$(document).ready(() => {
  $('div#add_item').click(() => {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(() => {
    $('ul.my_list li').last().remove();
  });
  $('div#clear_list').click(() => {
    $('ul.my_list').empty();
  });
});
