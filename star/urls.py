from django.conf.urls import url, include

from star.modules.Mars import urls as Mars_urls
from star.modules.user import urls as user_urls

urlpatterns = [
    url('mars/', include(Mars_urls)),
    url('user/', include(user_urls)),
]
