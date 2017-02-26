from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [

    # Perfil de usuario
    url(
        regex=r'^profile/$',
        view=views.ProfileIndexView.as_view(),
        name='profile'
    ),
]
