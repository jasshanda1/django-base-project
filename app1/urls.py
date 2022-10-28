from inspect import signature
from django.urls import path
from .views import *

app_name = 'app1'

urlpatterns = [
    # path('auth/user-list/', UserList.as_view(), name='user-list'),
    path('auth/sign-up/',signup.as_view(),name = 'sign-up'),
    path('auth/sign-in/',signin.as_view(),name = 'sign-up')
  
]