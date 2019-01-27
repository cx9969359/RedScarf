from rest_framework.views import APIView
from rest_framework.response import Response

from RedScarf.authentication_and_permission.authentication import ExpireAuthentication


class MarsView(APIView):
    authentication_classes = (ExpireAuthentication,)

    def post(self, request, *args, **kwargs):
        print(request.user)
        return Response(
            data={'result': 'success', 'description': 'nice,you have arrived here'},
            content_type='application/json'
        )
