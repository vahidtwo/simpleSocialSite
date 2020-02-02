from accounts.models import User
from like.models import Like
from like.serializers import LikeSerializer
from posts.models import Post
from django.http import JsonResponse
from rest_framework.status import (
	HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class Likes(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		_request_params = dict(request.data)
		_request_params['owner'] = request.user.id
		try:
			post = Post.objects.get(pk=_request_params.get('post'))
		except Post.DoesNotExist:
			return JsonResponse(data={'msg': 'post not correctly send ', 'success': False}, status=HTTP_400_BAD_REQUEST)
		try:
			like = Like.objects.get(post_id=post.id, owner=request.user)
			like.delete()
			if _request_params.get('value') == like.value:
				return JsonResponse(data={'msg': 'like or dislike deleted', 'success': True}, status=HTTP_200_OK)
			else:
				raise Like.DoesNotExist
		except Like.DoesNotExist:
			ser = LikeSerializer(data=_request_params)
			if ser.is_valid():
				ser_data = ser.data
				ser_data['owner'] = request.user
				try:
					ser_data['post'] = post
				except Post.DoesNotExist:
					return JsonResponse(data={'msg': 'post not correctly send ', 'success': False},
										status=HTTP_400_BAD_REQUEST)
				Like.objects.create(**ser_data)
				if ser_data.get('value') == 1:
					return JsonResponse(data={'msg': 'liked', 'success': True}, status=HTTP_201_CREATED)
				return JsonResponse(data={'msg': 'disLiked', 'success': True}, status=HTTP_201_CREATED)
			else:
				return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)
