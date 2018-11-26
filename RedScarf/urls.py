from django.conf.urls import url, include

from star.modules.Mars import urls as Mars_urls

urlpatterns = [
    url('star/', include(Mars_urls)),
]
