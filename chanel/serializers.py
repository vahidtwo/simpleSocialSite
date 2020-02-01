from rest_framework import serializers
from .models import Chanel
from accounts.serializers import UserSerializer


class ChanelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    author = UserSerializer(read_only=True, many=True)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.identifier = validated_data.get('identifier', instance.identifier)
        instance.save()
        return instance

    class Meta:
        model = Chanel
        fields = '__all__'
