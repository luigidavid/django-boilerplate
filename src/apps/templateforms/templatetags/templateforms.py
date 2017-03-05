from django import template
from django.template.loader import get_template
from django.utils.html import format_html

from ..settings import TEMPLATEFORMS_DEFAULT_TEMPLATES as defaul_template

register = template.Library()

TEMPLATES = {
    'non_field_errors': 'templateforms/{}/non_field_errors.html'.format(defaul_template),
    'field': 'templateforms/{}/text.html'.format(defaul_template),
    'textarea': 'templateforms/{}/textarea.html'.format(defaul_template),
    'select': 'templateforms/{}/select.html'.format(defaul_template),
    'checkbox': 'templateforms/{}/checkbox.html'.format(defaul_template),
    'radio': 'templateforms/{}/radio.html'.format(defaul_template),
    'boolean': 'templateforms/{}/boolean.html'.format(defaul_template),
    'file': 'templateforms/{}/file.html'.format(defaul_template),
    'hidden': 'templateforms/{}/hidden.html'.format(defaul_template),
}


@register.simple_tag(name='form')
def form(form_, **kwargs):
    """Renderiza el formulario completo."""
    html_form = ''
    html_form += render_template(
        'non_field_errors',
        non_field_errors=form_.non_field_errors
    )
    for field in form_:
        html_form += form_field(field, **kwargs)
    return format_html(html_form)


@register.inclusion_tag(TEMPLATES['non_field_errors'])
def non_field_errors(non_field_errors):
    """Errores de nivel de formulario."""
    return {'non_field_errors': non_field_errors}


@register.inclusion_tag(TEMPLATES['hidden'])
def form_hidden_fields(hidden_fields):
    """Campos ocultos."""
    return {'hidden_fields': hidden_fields}


def get_widget_type(field):
    """Obtener el typo de widget del campo."""
    try:
        widget = field.field.widget
    except:
        raise ValueError('ERROR {}'.format(field))
    return widget


def render_template(template_name, **kwargs_context):
    """Renderiza un campo según el template_name."""
    template_name = kwargs_context.get('tpl_name', TEMPLATES[template_name])
    return get_template(template_name).render(kwargs_context)


def input_text(**kwargs):
    """Campos tipo text|date|email|etc."""
    kwargs['ftype'] = kwargs.get('ftype', 'text')
    return render_template('field', **kwargs)


def input_textarea(**kwargs):
    """Campos tipo textarea."""
    return render_template('textarea', **kwargs)


def input_select(**kwargs):
    """Campos tipo select."""
    return render_template('select', **kwargs)


def input_checkbox(**kwargs):
    """Campos tipo checkbox."""
    return render_template('checkbox', **kwargs)


def input_radio(**kwargs):
    """Campos tipo radio."""
    return render_template('radio', **kwargs)


def input_boolean(**kwargs):
    """Campos tipo boolean."""
    return render_template('boolean', **kwargs)


def input_file(**kwargs):
    """Campos tipo file."""
    return render_template('file', **kwargs)


@register.simple_tag(name='form_field')
def form_field(field, **kwargs):
    """Dependiendo del tipo de widget, renderida un template."""
    widget_type = get_widget_type(field).__class__.__name__
    if widget_type == 'HiddenInput':
        return str(field)
    kwargs['field'] = field
    if widget_type == 'Textarea':
        return input_textarea(**kwargs)
    elif widget_type == 'CheckboxInput':
        return input_checkbox(ftype='checkbox', **kwargs)
    elif widget_type == 'RadioSelect':
        return input_radio(**kwargs)
    elif widget_type == 'Select' or widget_type == 'ChoiceField':
        return input_select(**kwargs)
    elif widget_type == 'SelectMultiple' or widget_type == 'CheckboxSelectMultiple':
        return input_select(multiple=True, **kwargs)
    elif widget_type == 'NullBooleanSelect':
        return input_boolean(**kwargs)
    elif widget_type == 'FileInput' or widget_type == 'ClearableFileInput':
        return input_file(ftype='file', **kwargs)
    else:
        if widget_type == 'EmailInput':
            kwargs['ftype'] = 'email'
        elif widget_type == 'NumberInput':
            kwargs['ftype'] = 'number'
        elif widget_type == 'DateInput':
            kwargs['ftype'] = 'date'
        elif widget_type == 'DateTimeInput':
            kwargs['ftype'] = 'datetime'
        elif widget_type == 'TimeInput':
            kwargs['ftype'] = 'time'
        elif widget_type == 'PasswordInput':
            kwargs['ftype'] = 'password'
        elif widget_type == 'URLInput':
            kwargs['ftype'] = 'url'
        kwargs['ftype'] = kwargs.get('ftype', 'text')
        return input_text(**kwargs)
