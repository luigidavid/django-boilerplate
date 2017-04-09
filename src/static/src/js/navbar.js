/**
 * Campo del buscador en la barra de navegacion superior.
 */
$(document).ready(function() {
  // Barra principal de navegacion materializecss
  $('.button-collapse').sideNav();

  // Al hacer scroll hacia abajo, esconde la barra.
  // Al subir la muestra.
  let position = $(window).scrollTop();

  $(window).scroll(function() {
    const scroll = $(window).scrollTop();

    if (scroll > position) {
      $('#navbar-main').removeClass('navbar-fixed');
    } else {
      $('#navbar-main').addClass('navbar-fixed');
    }

    position = scroll;
  });

  // Mustra el campo al pulsar en el icono de lupa.
  $('#navbar-search-button').on('click', function() {
    $('#navbar-search-field').removeClass('hide');
    $('#q').focus();
    // Si pierde focus el campo, lo ocultara.
    $('#q').focusout(function() {
      $('#navbar-search-field').addClass('hide');
    });
  });

  // Oculta el campo al pulsar la 'X' en el campo de busqueda.
  $('#navbar-search-field-close').on('click', function() {
    $('#navbar-search-field').addClass('hide');
  });
});
