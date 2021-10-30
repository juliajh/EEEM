from django.urls import path
from main import views
from .views import *

urlpatterns = [
    path("logout/", logout_view, name="logout"),
    path("login/", login_view, name="login"),
    path("signUp/", signUp_view, name="signUp"),
]
