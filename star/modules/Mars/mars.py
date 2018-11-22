from rest_framework.decorators import api_view
from rest_framework.response import Response


class MarsView():

    @api_view()
    def post(self):
        return Response(
            data='Nice,you have arrived here!'
        )

    def get_env(self):
        pass


if __name__ == '__main__':
    mar = MarsView()
    mar.get_env()
