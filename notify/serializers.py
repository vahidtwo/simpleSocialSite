from rest_framework import serializers
from .models import Notify
from accounts.serializers import UserSerializer


class NotifySerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)

	class Meta:
		model = Notify
		fields = '__all__'
