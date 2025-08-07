from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class JwtService:
    def __init__(self, user: User):
        self.user = user

    def get_token(self) -> RefreshToken:
        if not User.objects.filter(id=self.user.id).exists():
            raise ValueError("User does not exist")

        user = self.user

        token: RefreshToken = RefreshToken.for_user(self.user)
        token["username"] = self.user.username
        token["email"] = self.user.email
        return token
