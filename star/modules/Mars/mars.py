from rest_framework.decorators import api_view
from rest_framework.response import Response


class MarsView():

    @api_view()
    def post(self):
        return Response(
            data='Nice,you have arrived here!'
        )
