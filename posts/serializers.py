from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

    class Meta:
        model = Post
        fields = '__all__'
