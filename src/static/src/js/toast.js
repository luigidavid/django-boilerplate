// Cerrar el toast.
$(document).on('click', '#toast-container .toast', function() {
  $(this).fadeOut(function() {
    $(this).remove();
  });
});
