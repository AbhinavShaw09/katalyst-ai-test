from django.contrib.auth.models import User
from api.tests.base import BaseAPITestCase

from api.services.jwt import JwtService


class JwtServiceTests(BaseAPITestCase):
    def setUp(self):
        self.user = self.make_model(
            User,
            username="testuser",
            password="securepass",
        )
        self.user.name = "Test User"
        self.user.email = "test@example.com"
        self.user.save()

    def test_token_creation_user(self):
        service = JwtService(self.user)
        token = service.get_token()
        self.assertIsNotNone(token) 
 
    def test_token_fields_match_user(self):
        service = JwtService(self.user)
        token = service.get_token()

        self.assertEqual(token["username"], self.user.username)

    def test_raises_error_for_invalid_user(self):
        service = JwtService(self.user)
        User.objects.filter(id=self.user.id).delete()

        with self.assertRaises(ValueError):
            service.get_token()