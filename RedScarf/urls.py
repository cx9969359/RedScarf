from django.conf.urls import url, include

from star import urls as star_urls

urlpatterns = [
    url('star/', include(star_urls)),
]
