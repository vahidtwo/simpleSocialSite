from rest_framework import serializers
from like.models import Like
from .models import Post
from django.db.models import Sum


class PostSerializer(serializers.ModelSerializer):
	like = serializers.SerializerMethodField()

	def get_like(self, obj):
		if type(obj) is Post:
			if obj._meta is Post._meta:
				liked = Like.objects.filter(post_id=obj.id, value=1).aggregate(Sum('value'))['value__sum']
				dislike = Like.objects.filter(post_id=obj.id, value=-1).aggregate(Sum('value'))['value__sum']
				liked = liked if liked else 0
				dislike = dislike if dislike else 0
				return {'liked': liked, 'disLiked': dislike}
		return {'liked': 0, 'disLiked': 0}

	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.body = validated_data.get('body', instance.body)
		instance.save()
		return instance

	class Meta:
		model = Post
		fields = '__all__'
