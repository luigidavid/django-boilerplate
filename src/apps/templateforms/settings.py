from django.conf import settings

TEMPLATEFORMS_DEFAULT_TEMPLATES = getattr(
    settings, 'TEMPLATEFORMS_DEFAULT_TEMPLATES', 'materializecss'
)
