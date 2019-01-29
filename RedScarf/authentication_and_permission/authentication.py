from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from star.models import TokenObject


class ExpireAuthentication(BaseAuthentication):
    """
    自定义认证权限
    todo 将token存入缓存并设定期限
    """

    def authenticate(self, request):
        # request._request为原生request
        token = request._request.GET.get('token', None)
        try:
            token_obj = TokenObject.objects.get(token=token)
            user = token_obj.user
        except Exception:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (user, token)

    def authenticate_header(self, request):
        pass
