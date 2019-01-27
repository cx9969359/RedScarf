from rest_framework.views import APIView
from rest_framework.response import Response


class MarsView(APIView):

    def post(self, request, *args, **kwargs):
        return Response(
            data={'result': 'success', 'description': 'nice,you have arrived here'},
            content_type='application/json'
        )
