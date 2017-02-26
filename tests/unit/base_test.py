import json
import os

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

UserModel = get_user_model()


class BaseTestCase(TestCase):
    """Base para test.

    Attributes:
        fixtures (list): Nombres de fixtures a leer, incluida la extensión.
    """
    fixtures = [
        'accounts.json',
        'sites.json'
    ]

    def setUp(self):
        super().setUp()
        self.user_model = UserModel

    def resolve_url(self, urlconf, *args, **kwargs):
        """Optener el reverse de un URLConf.

        Args:
            urlconf (str): El string del URLConf.
            *args: Lista de argumentos para reverse.
            **kwargs: Diccionario para reverse.
        """
        return reverse(urlconf, *args, **kwargs)

    def login(self, username=None, password=None):
        """Login de usuario.

        Si no se pasa username y password usara por defecto
        snicoper y 123 respectivamente.

        Args:
            username (str): Nombre de usuario.
            password (str): Password de usuario.
        """
        username = 'snicoper' if username is None else username
        password = '123' if password is None else password
        login = self.client.login(username=username, password=password)

        self.assertTrue(login)

    def logout(self):
        self.client.logout()

    def load_data(self, path_data):
        """Obtener de un .json datos.

        Args:
            path_data (str): path con el archivo a leer.

        Returns:
            dict: Diccionario con los datos del json

        Raises:
            FileNotFoundError: Si no existe el .json en el la ruta indicada.
        """
        if not os.path.exists(path_data):
            raise FileNotFoundError
        with open(path_data, 'r') as fh:
            data = json.load(fh)
        return data
