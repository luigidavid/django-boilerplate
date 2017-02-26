from django.contrib.sites.models import Site


def common_template_vars(request):
    """Variables comunes en los templates."""
    return {
        'SITE': Site.objects.get_current(),
    }
