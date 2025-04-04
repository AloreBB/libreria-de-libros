from django.urls import path
from django.contrib.auth.decorators import login_not_required

from . import views

urlpatterns = [
    path("registro/", login_not_required(views.registro_view), name="registro"),
    path("login/", login_not_required(views.login_view), name="login"),
    path("logout/", views.logout_view, name="logout"),
]
