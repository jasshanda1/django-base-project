from rest_framework import serializers
from app1.models.UserModel import User


class UserCreateUpdateSerializer(serializers.ModelSerializer):
	"""
	create/update user .
	"""
	id = serializers.IntegerField(required=False)
	class Meta:
		model = User
		fields = ('id', 'first_name', 'phone_no', 'email', 'country_code', 'gender', 'address', 'longitude', 'latitude')       

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