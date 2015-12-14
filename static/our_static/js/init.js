(function($){
  $(function(){

    $('.button-collapse').sideNav();

  }); // end of document ready
})(jQuery); // end of jQuery name space

// Toggle search

$('a#toggle-search').click(function()
{
    var search = $('div#search');

    search.is(":visible") ? search.slideUp() : search.slideDown(function()
    {
        search.find('input').focus();
    });

    return false;
});

$('.modal-trigger').leanModal();
$('#aside').pushpin({ top:110, bottom:500 });