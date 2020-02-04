from notify.models import Notify
from posts.models import Post
from .models import Comment
from django.http import JsonResponse
from rest_framework.status import (
	HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
)
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Helper.permission import IsOwner


class Comments(APIView):
	permission_classes = (IsAuthenticated, IsOwner)

	def post(self, request):
		_request_params = dict(request.data)
		_request_params['owner'] = request.user.id
		try:
			comment = ''
			post = Post.objects.get(pk=_request_params.get('post'))
			if _request_params.get('comment'):
				comment = Comment.objects.get(pk=_request_params['comment'])
		except (Post.DoesNotExist, Comment.DoesNotExist):
			return JsonResponse(data={'msg': 'post or comment id is not correct', 'success': False},
			                    status=HTTP_400_BAD_REQUEST)
		ser = CommentSerializer(data=_request_params)
		if ser.is_valid():
			ser_data = ser.data
			ser_data['owner'] = request.user
			ser_data['post'] = post
			ser_data['comment'] = comment
			if not comment:
				ser_data.pop('comment')
			comment = Comment.objects.create(**ser_data)
			Notify.objects.create(**{'user': post.author, 'body': 'you have a comment of {}'.
			                      format(request.user.get_username()),
			                         "link": "{}/api/comment/get/".format(request.get_host()) + str(comment.id)})
			return JsonResponse(data={'msg': 'comment create', 'success': True}, status=HTTP_201_CREATED)
		else:
			return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)

	def put(self, request, pk):
		_request_params = dict(request.data)
		try:
			comment = Comment.objects.get(pk=pk)
			self.check_object_permissions(request, comment)
		except Comment.DoesNotExist:
			return JsonResponse(data={'msg': 'comment id is not correct', 'success': False},
			                    status=HTTP_400_BAD_REQUEST)
		ser = CommentSerializer(comment, _request_params, partial=True)
		if ser.is_valid():
			ser.save()
			return JsonResponse(data={'msg': 'comment is update', 'success': True},
			                    status=HTTP_200_OK)
		else:
			return JsonResponse(data={'msg': ser.errors, 'success': False},
			                    status=HTTP_400_BAD_REQUEST)

	def get(self, request, post_id=None):
		comment = Comment.objects.filter(post_id=post_id)
		data = CommentSerializer(comment, many=True).data
		return JsonResponse(data={'data': data, 'success': True},
		                    status=HTTP_200_OK)

	def delete(self, request, pk=None):
		try:
			comment = Comment.objects.get(pk=pk)
			self.check_object_permissions(request, comment)
			comment.delete()
			return JsonResponse(data={'msg': 'comment delete', 'success': True},
			                    status=HTTP_200_OK)
		except Comment.DoesNotExist:
			return JsonResponse(data={'msg': 'comment id is not correct', 'success': False},
			                    status=HTTP_400_BAD_REQUEST)
