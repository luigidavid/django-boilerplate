from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

from home.views import IndexView

urlpatterns = [
    ##################################################
    # / Home page.
    url(r'^$', IndexView.as_view(), name='home_page'),
    ##################################################

    # /accounts/*
    url(r'^accounts/', include('accounts.urls')),

    # /auth/*
    url(r'^auth/', include('authentication.urls')),

    # /home/*
    url(r'^home/', include('home.urls')),

    # /pages/*
    url(r'^pages/', include('pages.urls')),

    # /admin/*
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    import debug_toolbar

    urlpatterns += [
        # /media/:<mixed>path/
        url(
            regex=r'^media/(?P<path>.*)$',
            view=serve,
            kwargs={'document_root': settings.MEDIA_ROOT}
        ),

        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
