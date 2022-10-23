from django.urls import path
from .views import *

app_name = 'app1'

urlpatterns = [
    path('auth/user-list/', UserList.as_view(), name='user-list'),
  
]