from django.http import JsonResponse
from rest_framework.status import (
	HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from accounts.serializers import UserSerializer
from chanel.models import Chanel


class UserAPI(APIView):
	permission_classes = (IsAuthenticated,)

	def put(self, request):
		_request_perms = request.data
		user = request.user
		ser = UserSerializer(user, _request_perms)
		if ser.is_valid():
			ser.save()
			return JsonResponse(data={'msg': 'user update', 'success': True}, status=HTTP_200_OK)
		else:
			return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)

	def get(self, request, username=None):
		if username:
			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist:
				return JsonResponse(data={'msg': 'user not found', 'success': False}, status=HTTP_404_NOT_FOUND)
			return JsonResponse(data={'data': UserSerializer(user).data, 'success': True}, status=HTTP_200_OK)
		else:
			return JsonResponse(data={'data': UserSerializer(request.user).data, 'success': True}, status=HTTP_200_OK)
