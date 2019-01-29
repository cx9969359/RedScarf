from rest_framework import serializers

from star.models import User


class SignInValidator(serializers.Serializer):
    username = serializers.RegexField(regex='^[a-zA-Z0-9_\u4e00-\u9fa5-+#*%@!]+$', max_length=32, allow_blank=False)
    password = serializers.CharField(max_length=128, allow_blank=False)

    def validate(self, attrs):
        user_list = User.objects.filter(username=attrs['username'])
        if user_list.count() > 0:
            msg = {'result': 'The username has existed'}
            raise Exception(msg)
        return attrs
