from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from app1.models.UserModel import User
from app1.serializers.UserSerializer import UserCreateUpdateSerializer,UserLoginDetailSerializer
from rest_framework import generics
from app1.models.UserSessionModel import UserSession
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
                user_session = self.create_update_user_session(user, refresh, request)
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


    def create_update_user_session(self, user, token, request):
        """
        Create User Session
        """
        if "device-token" in request.data:
            device_id = request.data.get('device-id'),
            device_type = request.data.get('device-type'),
            app_version = request.data.get('app-version'),
            device_token = request.data.get('device-token')

        else: 
            device_id = request.headers.get('device-id'),
            device_type = request.headers.get('device-type'),
            app_version = request.headers.get('app-version'),
            device_token = request.headers.get('device-token')

        user_session = self.get_user_session_object(user.pk, device_id)

        if user_session is None:
            UserSession.objects.create(
                user = user,
                token = token,
                device_id = device_id,
                device_type = device_type,
                app_version = app_version,
                device_token = device_token,
            )

        else:
            user_session.token = token
            user_session.app_version = app_version
            user_session.save()

        return user_session

    def get_user_session_object(self, user_id, device_type=None, device_token=None, device_id=None):
        try:
            if device_id:
                try:
                    return UserSession.objects.get(user=user_id, device_type=device_type, device_id=device_id, device_token=device_token)
                except UserSession.DoesNotExist:
                    return None

            return UserSession.objects.get(user=user_id, device_type=device_type, device_id=device_id, device_token=device_token)

        except UserSession.DoesNotExist:
            return None