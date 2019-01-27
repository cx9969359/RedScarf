from django.conf.urls import url
from star.modules.Mars import mars_view

urlpatterns = [
    url(r'^mars$', mars_view.MarsView.as_view()),
]
