from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from django.core.cache import cache

from star.models import Token


class ExpireAuthentication(BaseAuthentication):
    """
    自定义认证权限
    """

    def authenticate(self, request):
        # request._request为原生request
        token = request._request.GET.get('token', None)
        try:
            token = Token.objects.get(token=token)
            user = token.user
        except Exception:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (user,token)

    def authenticate_header(self, request):
        pass
