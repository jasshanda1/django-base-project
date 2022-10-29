from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from app1.models.UserModel import User
from app1.serializers.UserSerializer import UserCreateUpdateSerializer,UserLoginDetailSerializer
from rest_framework import generics
import jwt
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import AllowAny
from base import settings 
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError

from rest_framework import status

def create_object_serilaizer(serializer, message):
    if serializer.is_valid():
        serializer.save()
        return Response({"data":serializer.data, "code":201, "message":message})
    return Response({"data":serializer.errors, "code":status.HTTP_400_BAD_REQUEST, "message":"Oops! Something went wrong."})    

class signup(APIView):
    serializer_class = UserCreateUpdateSerializer
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        return create_object_serilaizer(serializer, "User Created Successfully")

    
    
class Login(APIView):
    serializer_class = UserLoginDetailSerializer
    permission_classes = (AllowAny,)
    def post(self,request,format = None):
        username = request.data['email']
        username = username.lower()
        password = request.data['password']
        user = self.user_authenticate(username, password)
        if user is not None:
                login(request, user)
                serializer = self.serializer_class(user)
                refresh = RefreshToken.for_user(user)
                user_details = serializer.data
                return Response({"data": user_details,"code": status.HTTP_200_OK,"message": "LOGIN_SUCCESSFULLY",'refresh': str(refresh),'access': str(refresh.access_token)})
        return Response({"data": None,"code": status.HTTP_400_BAD_REQUEST, "message": "INVALID_CREDENTIALS"})

    def user_authenticate(self,username,password):
        try:
            user = User.objects.get(email= username)
            if user.check_password(password):
                return user # return user on valid credentials
        except User.DoesNotExist:
            try:
                user = User.objects.get(phone_no=username)
                if user.check_password(password):
                    return user # return user on valid credentials
            except User.DoesNotExist:
                return None



