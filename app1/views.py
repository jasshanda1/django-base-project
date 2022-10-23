from app1.models.UserModel import User
from app1.serializers.UserSerializer import UserCreateUpdateSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class UserList(generics.ListAPIView,generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer