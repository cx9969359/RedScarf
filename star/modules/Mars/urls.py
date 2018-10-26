from django.conf.urls import url
from star.modules.Mars import mars

urlpatterns = [
    url(
        r'^mars$',
        mars.MarsView.post
    ),
]
