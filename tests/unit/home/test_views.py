from django.urls import reverse

from tests.unit.base_test import BaseTestCase


class IndexViewTest(BaseTestCase):

    def test_200_home_page(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)

    def test_200_home_index(self):
        response = self.client.get(reverse('home:index'))
        self.assertEqual(response.status_code, 200)
