from rest_framework.authentication import BaseAuthentication


class ExpireAuthentication(BaseAuthentication):
    """
    自己实现权限验证
    """

    def authenticate(self, request):
        return request
