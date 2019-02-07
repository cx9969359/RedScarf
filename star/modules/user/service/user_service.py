import hashlib
import time
from django.conf import settings

from django.core.cache import cache

from star.models import User
from star.modules.common.key_service import KeyService


class TokenService():

    def check_user_and_create_token(self, username, password):
        """
        检查用户信息并签发token
        :param username:
        :param password:
        :return:
        """
        # 系统中用户名唯一
        try:
            user = User.objects.get(username=username)
        except Exception:
            raise Exception('无效用户')
        if user.password != password:
            raise Exception('密码错误，请重新输入')
        user_token_key = KeyService().get_user_token_key(user)
        token = cache.get(user_token_key)
        if not token:
            token = self.create_token(user.username)
            token_timeout = settings.TOKEN_CACHES_TIMEOUT
            cache.set(user_token_key, token, token_timeout)
        return token

    def create_token(self, username):
        current_timestamp = str(time.time())
        md = hashlib.md5()
        md.update((current_timestamp + username).encode('utf-8'))
        return md.hexdigest()
