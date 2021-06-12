from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
import account.views as views


app_name = 'account'
urlpatterns = [
    path('login/', obtain_auth_token),
]
