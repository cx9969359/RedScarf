from rest_framework.views import APIView
from rest_framework.response import Response

from star.models import User
from star.modules.user.serializer.user_serializer import SignInValidator
from star.modules.user.service.user_service import TokenService


class RegisterUserView(APIView):
    """
    注册用户
    """

    def post(self, request, *args, **kwargs):
        validator = SignInValidator(data=request.data, context={'request': request})
        validator.is_valid(raise_exception=True)
        username = validator.data['username']
        password = validator.data['password']
        user = User(username=username, password=password)
        user.save()

        return Response(
            data={'result': 'success'},
            content_type='application/json'
        )


class LoginUserView(APIView):
    """
    用户登录并签发token
    todo token的缓存，过期删除
    """

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        token = TokenService().check_user_and_create_token(username, password)

        return Response(
            data={'result': 'success', 'token': token},
            content_type='application/json'
        )
