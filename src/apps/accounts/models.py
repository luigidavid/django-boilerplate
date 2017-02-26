from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """Model para usuarios."""

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
