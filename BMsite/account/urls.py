from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


app_name = 'account'
urlpatterns = [
    path('login/', obtain_auth_token),
]
