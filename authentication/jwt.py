from jwt.exceptions import DecodeError, ExpiredSignatureError
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings
from authentication.models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization', None)
        if not auth_header or len(auth_header.split(' ')) != 2:
            raise AuthenticationFailed('Unauthorized')
        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
            email = payload['email']
            user = User.objects.get(email=email)
            return (user, token)
        except ExpiredSignatureError:
            raise AuthenticationFailed('Session expired')
        except DecodeError:
            raise AuthenticationFailed('Unauthorized')
