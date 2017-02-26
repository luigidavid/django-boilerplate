from django.views import generic


class ProfileIndexView(generic.TemplateView):
    template_name = 'accounts/profile.html'
