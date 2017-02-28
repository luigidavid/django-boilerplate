from django import template
from django.utils.safestring import mark_safe

import markdown2

register = template.Library()


@register.filter('markdown')
def markdown_format(text):
    """Devuelve el texto markdown en HTML.

    Por defecto, materializecss elimina los 'estilos'
    de las listas, el replace, es solo útil si se
    esta usando materializecss.

    Example:
        {{ obj.body|markdown }}

    Args:
        text (str): Texto markdown

    Returns:
        str: El markdown convertido en HTML.
    """
    return mark_safe(
        markdown2.markdown(
            text,
            extras=['fenced-code-blocks']
        ).replace('<ul>', '<ul class="browser-default ul-default">')
    )
