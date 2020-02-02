from rest_framework import serializers

from posts.serializers import PostSerializer
from .models import Comment
from accounts.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    def validate_post(self, attrs):
        if not attrs:
            raise serializers.ValidationError('post not send ')

    def validate_comment(self, attrs):
        if not dict(self.initial_data).get('post'):
            if not attrs:
                raise serializers.ValidationError('comment not send ')

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

    class Meta:
        model = Comment
        fields = '__all__'
