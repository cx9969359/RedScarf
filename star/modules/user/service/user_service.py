import hashlib
import time

from star.models import User


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
        token = self.get_token(username)
        return token

    def get_token(self, username):
        """
        根据当前时间生成token
        :param username:
        :return:
        """
        current_timestamp = str(time.time())
        md = hashlib.md5()
        md.update((current_timestamp + username).encode('utf-8'))
        return md.hexdigest()
