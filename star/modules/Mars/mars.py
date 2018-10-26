from rest_framework import permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class MarsView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    @api_view()
    def post(self):
        return Response(
            data='Nice'
        )
