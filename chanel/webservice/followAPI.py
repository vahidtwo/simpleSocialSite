from django.http import JsonResponse
from rest_framework.status import (
	HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
)

from notify.models import Notify
from ..serializers import ChanelSerializer, FollowSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Helper.permission import IsOwner
from chanel.models import Chanel, Follow


class Following(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request, identifier=None):
		_request_params = request.data
		_request_params['user'] = request.user.id
		try:
			chanel = Chanel.objects.get(identifier=identifier)
			_request_params['chanel'] = chanel.id
		except Chanel.DoesNotExist:
			return JsonResponse(data={'msg': 'chanel identifier not found', 'success': False},
			                    status=HTTP_400_BAD_REQUEST)
		ser = FollowSerializer(data=_request_params)
		if ser.is_valid():
			try:
				follow = Follow.objects.get(user=request.user, chanel=chanel)
				follow.delete()
				return JsonResponse(data={'msg': 'you unFollow {}'.format(follow.chanel.identifier), 'success': True},
				                    status=HTTP_201_CREATED)
			except Follow.DoesNotExist:
				follow = Follow.objects.create(**{'user': request.user, 'chanel': chanel})
				Notify.objects.create(**{'user': follow.chanel.owner, 'body': 'you follow by {}'.
				                      format(request.user.get_username()),
				                         "link": "{}/api/chanel/get/".format(request.get_host()) + str(follow.chanel.identifier)})
				return JsonResponse(data={'msg': 'you follow {}'.format(follow.chanel.identifier), 'success': True},
				                    status=HTTP_201_CREATED)
		else:
			return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)
