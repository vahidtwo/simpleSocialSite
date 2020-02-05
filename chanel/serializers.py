from rest_framework import serializers
from .models import Chanel, Follow
from accounts.serializers import UserSerializer


class ChanelSerializer(serializers.ModelSerializer):
	owner = UserSerializer(read_only=True)
	author = UserSerializer(read_only=True, many=True)

	def update(self, instance, validated_data):
		instance.description = validated_data.get('description', instance.description)
		instance.identifier = validated_data.get('identifier', instance.identifier)
		instance.law = validated_data.get('law', instance.law)
		instance.title = validated_data.get('title', instance.title)
		instance.save()
		return instance

	class Meta:
		model = Chanel
		fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
	def to_representation(self, instance):
		ret = super(FollowSerializer, self).to_representation(instance)
		ret['chanel'] = {'identifier': instance.chanel.identifier, 'id':instance.chanel.id}
		return ret

	class Meta:
		model = Follow
		fields = '__all__'
