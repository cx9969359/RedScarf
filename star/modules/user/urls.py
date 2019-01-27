from django.conf.urls import url
from star.modules.user.view import user_views

urlpatterns = [
    url(r'^register$', user_views.RegisterUserView.as_view()),
    url(r'^login$', user_views.LoginUserView.as_view()),
]
