import hashlib
import time

from star.models import User, TokenObject


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
        token = self.get_token(user)
        return token

    def get_token(self, user):
        """
        查找或生成token
        :param user:
        :return:
        """
        username = user.username
        token_set = TokenObject.objects.filter(user=user)
        if token_set.count() > 0:
            token_obj = token_set[0]
            token = token_obj.token
        else:
            token = self.create_token(username)
            token_obj = TokenObject(token=token, user=user)
            token_obj.save()
        return token

    def create_token(self, username):
        current_timestamp = str(time.time())
        md = hashlib.md5()
        md.update((current_timestamp + username).encode('utf-8'))
        return md.hexdigest()
