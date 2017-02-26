from django.test import TestCase

from core import text


class UtilsTextTest(TestCase):

    def test_ucfirst(self):
        """La primera letra en mayusculas."""
        texto = 'hola mundo'
        self.assertEqual(text.ucfirst(texto), 'Hola mundo')

    def test_ucfirst_letter(self):
        """La primera letra de cada palabra en mayus."""
        texto = 'hola mundo'
        self.assertEqual(text.ucfirst_letter(texto), 'Hola Mundo')
