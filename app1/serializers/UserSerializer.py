from rest_framework import serializers
from app1.models.UserModel import User
from rest_framework.response import Response



class UserCreateUpdateSerializer(serializers.ModelSerializer):
    """
    create/update user .
    """
    id = serializers.IntegerField(required=False)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'phone_no', 'email', 'country_code', 'gender', 'address', 'longitude', 'latitude')       

    def validate(self, data):
        
        email  = User.objects.filter(email=data.get('email'))
        phone = User.objects.filter(phone_no=data.get('phone_no'))
        if email:
            raise serializers.ValidationError('email already exists')
        if phone:
            raise serializers.ValidationError('phone_no already exists')
        return data




        
    

    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data['first_name']
        instance.email = validated_data['email']
        instance.country_code = validated_data['country_code']
        instance.phone_no = validated_data['phone_no']
        instance.address = validated_data['address']
        if 'longitude' in validated_data:
            instance.longitude = validated_data['longitude']
        if 'latitude' in validated_data:
            instance.latitude = validated_data['latitude']
        instance.gender = validated_data['gender']
        instance.save()

        
        return instance

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.email = validated_data['email']
        instance.country_code = validated_data['country_code']
        instance.phone_no = validated_data['phone_no']
        instance.address = validated_data['address']
        if 'longitude' in validated_data:
            instance.longitude = validated_data['longitude']
        if 'latitude' in validated_data:
            instance.latitude = validated_data['latitude']
        instance.gender = validated_data['gender']
        instance.save()

        
        return instance

class UserLoginDetailSerializer(serializers.ModelSerializer):
    """
    Return the details of Login User.
    """
    # dob = serializers.DateField(format=DATEFORMAT, input_formats=[DATEFORMAT])

    class Meta(object):
        model = User
        fields = (
        'id', 'email', 'first_name', 'last_name', 'phone_no', 'is_active', 'is_deleted','otp_varification')

