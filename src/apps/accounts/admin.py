from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import ugettext_lazy as _

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    """User en admin."""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        (_('Información personal'), {
            'fields': ('first_name', 'last_name', 'email')
        }),
        (_('Permisos'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        (_('Fechas importantes'), {
            'fields': ('last_login', 'date_joined')
        }),
    )
