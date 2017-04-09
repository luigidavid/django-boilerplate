$(document).ready(function() {
  // close alert messages
  (function() {
    $('.close-alert').on('click', function() {
      $(this).parent().fadeOut(400, function() {
        $(this).remove();
      });
    });
  })();
});
