'use strict';

$(document).ready(function () {
  // close alert messages
  (function () {
    $('.close-alert').on('click', function () {
      $(this).parent().fadeOut(400, function () {
        $(this).remove();
      });
    });
  })();
});

'use strict';

$(document).ready(function () {});

'use strict';

/**
 * Campo del buscador en la barra de navegacion superior.
 */
$(document).ready(function () {
  // Barra principal de navegacion materializecss
  $('.button-collapse').sideNav();

  // Al hacer scroll hacia abajo, esconde la barra.
  // Al subir la muestra.
  var position = $(window).scrollTop();

  $(window).scroll(function () {
    var scroll = $(window).scrollTop();

    if (scroll > position) {
      $('#navbar-main').removeClass('navbar-fixed');
    } else {
      $('#navbar-main').addClass('navbar-fixed');
    }

    position = scroll;
  });

  // Mustra el campo al pulsar en el icono de lupa.
  $('#navbar-search-button').on('click', function () {
    $('#navbar-search-field').removeClass('hide');
    $('#q').focus();
    // Si pierde focus el campo, lo ocultara.
    $('#q').focusout(function () {
      $('#navbar-search-field').addClass('hide');
    });
  });

  // Oculta el campo al pulsar la 'X' en el campo de busqueda.
  $('#navbar-search-field-close').on('click', function () {
    $('#navbar-search-field').addClass('hide');
  });
});

// Cerrar el toast.
$(document).on('click', '#toast-container .toast', function () {
  $(this).fadeOut(function () {
    $(this).remove();
  });
});

'use strict';

// to-top
(function () {
  var offset = 220;
  var duration = 500;

  jQuery(window).scroll(function () {
    if (jQuery(this).scrollTop() > offset) {
      jQuery('.to-top').fadeIn(duration);
    } else {
      jQuery('.to-top').fadeOut(duration);
    }
  });

  jQuery('.to-top').click(function (event) {
    event.preventDefault();
    jQuery('html, body').animate({ scrollTop: 0 }, duration);
    return false;
  });
})();
//# sourceMappingURL=main.js.map
