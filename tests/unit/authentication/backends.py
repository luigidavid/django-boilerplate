from django.core.urlresolvers import reverse

from .base_auth import BaseAuthTest


class EmailOrUsernameModelBackend(BaseAuthTest):

    def setUp(self):
        super().setUp()
        self.urlconf = reverse('authentication:login')
        self.user = self.user_model.objects.get(pk=1)

    def test_auth_username(self):
        """Prueba un login con username, es el default."""
        form_data = {
            'username': self.user.username,
            'password': '123'
        }
        response = self.client.post(self.urlconf, data=form_data, follow=True)
        expected_url = reverse('accounts:profile')

        self.assertRedirects(
            response=response,
            expected_url=expected_url,
            status_code=302,
            target_status_code=200
        )

    def test_auth_email(self):
        """No permite login con email."""
        form_data = {
            'email': self.user.email,
            'password': '123'
        }
        response = self.client.post(self.urlconf, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
