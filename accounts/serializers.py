from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
	def update(self, instance, validated_data):
		instance.email = validated_data.get('email', instance.email)
		instance.phone_number = validated_data.get('phone_number', instance.phone_number)
		instance.city = validated_data.get('city', instance.city)
		instance.country = validated_data.get('country', instance.country)
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.username = validated_data.get('username', instance.username)
		instance.picture = validated_data.get('picture', instance.picture)
		instance.save()
		return instance

	def to_representation(self, instance):
		ret = super(UserSerializer, self).to_representation(instance)
		ret.pop('phone_number')
		ret.pop('email')
		return ret

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'picture', 'city', 'country', 'id', 'email',
		          'phone_number']
