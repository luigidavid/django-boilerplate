from django.contrib import messages
from django.views import generic


class IndexView(generic.TemplateView):
    """Pagina de prueba para home."""
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        """Prueba de messages."""
        messages.info(request, 'Three credits remain in your account.')
        messages.success(request, 'Profile details updated.')
        messages.warning(request, 'Your account expires in three days.')
        messages.error(request, 'Document deleted.')
        return super().get(request, *args, **kwargs)
