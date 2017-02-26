from django.contrib.sites.models import Site
from django.views import generic

from core.mixins.views import PageMixin

# EXAMPLE:
# class AboutView(PageMixin, generic.TemplateView):
#     template_name = 'pages/hello.html'
#     template_md = 'pages/hello.md'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['nombre'] = 'Perico palote'
#         return context
#
#     def get_context_md(self):
#         context = super().get_context_md()
#         context['hola'] = 'Hello world'
#         return context


class CookieConsentView(PageMixin, generic.TemplateView):
    """Muestra la politica de cookies."""
    template_name = 'pages/cookie_consent.html'
    template_md = 'pages/cookie_consent.md'

    def get_context_md(self):
        context = super().get_context_md()
        context['site'] = Site.objects.get_current()
        return context
