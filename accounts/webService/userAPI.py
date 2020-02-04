from django.http import JsonResponse
from rest_framework.parsers import FileUploadParser
from rest_framework.status import (
	HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from accounts.serializers import UserSerializer
from chanel.models import Follow
from chanel.serializers import FollowSerializer
from posts.models import Post


class UserAPI(APIView):
	permission_classes = (IsAuthenticated,)
	parser_class = (FileUploadParser,)

	def put(self, request):
		_request_perms = request.data
		try:
			_request_perms['title'] = str(_request_perms.get('picture').name)
		except Exception:
			pass
		user = request.user
		ser = UserSerializer(user, _request_perms, partial=True)
		if ser.is_valid():
			ser.save()
			return JsonResponse(data={'msg': 'user update', 'success': True}, status=HTTP_200_OK)
		else:
			return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)

	def get(self, request, username=None):
		data = {}
		data['user_post_count'] = Post.objects.filter(author=request.user).count()
		if username:
			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist:
				return JsonResponse(data={'msg': 'user not found', 'success': False}, status=HTTP_404_NOT_FOUND)
			follower = Follow.objects.filter(chanel__owner=user)
			following = Follow.objects.filter(user=user)
			data['follower'] = FollowSerializer(follower, many=True).data
			data['follower_count'] = follower.count()
			data['following'] = FollowSerializer(following, many=True).data
			data['following_count'] = following.count()

			data['user_data'] = UserSerializer(user).data
			return JsonResponse(data={'data': data, 'success': True}, status=HTTP_200_OK)
		else:
			data['user_data'] = UserSerializer(request.user).data
			follower = Follow.objects.filter(chanel__owner=request.user)
			following = Follow.objects.filter(user=request.user)
			data['follower'] = FollowSerializer(follower, many=True).data
			data['follower_count'] = follower.count()
			data['following'] = FollowSerializer(following, many=True).data
			data['following_count'] = following.count()
			return JsonResponse(data={'data': data, 'success': True}, status=HTTP_200_OK)
