from django.db.models import Sum
from rest_framework import serializers
from like.models import Like
from .models import Comment
from accounts.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
	owner = UserSerializer(read_only=True)
	like = serializers.SerializerMethodField()

	def get_like(self, obj):
		if type(obj) is Comment:
			if obj._meta is Comment._meta:
				liked = Like.objects.filter(comment_id=obj.id, value=1).aggregate(Sum('value'))['value__sum']
				dislike = Like.objects.filter(comment_id=obj.id, value=-1).aggregate(Sum('value'))['value__sum']
				liked = liked if liked else 0
				dislike = dislike if dislike else 0
				return {'liked': liked, 'disLiked': dislike}
		return {'liked': 0, 'disLiked': 0}

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
