from accounts.models import User
from notify.models import Notify
from django.http import JsonResponse
from rest_framework.status import (
	HTTP_400_BAD_REQUEST, HTTP_200_OK
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Helper.permission import IsOwner
from notify.serializers import NotifySerializer


class Notifier(APIView):
	permission_classes = (IsAuthenticated, IsOwner)

	def get(self, request, pk=None):
		if pk:
			try:
				notify = Notify.objects.get(pk=pk)
				self.check_object_permissions(request, notify)
				data = NotifySerializer(notify).data
				notify.is_read = True
				notify.save()
			except Notify.DoesNotExist:
				return JsonResponse(data={'msg': 'notify id is incorrect', 'success': False},
				                    status=HTTP_400_BAD_REQUEST)
		else:
			notify = Notify.objects.filter(user=request.user, is_read=False)
			data = NotifySerializer(notify, many=True).data
		return JsonResponse(data={'data': data, 'success': True},
			                    status=HTTP_200_OK)

