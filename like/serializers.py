from rest_framework import serializers
from .models import Like
from accounts.serializers import UserSerializer


class LikeSerializer(serializers.ModelSerializer):
	owner = UserSerializer(read_only=True)

	class Meta:
		model = Like
		fields = '__all__'
