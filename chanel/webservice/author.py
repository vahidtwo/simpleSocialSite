from django.http import JsonResponse
from rest_framework.status import (
	HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
)

from accounts.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Helper.permission import IsChanelOwner
from chanel.models import Chanel


class Author(APIView):
	permission_classes = (IsAuthenticated, IsChanelOwner)

	def post(self, request):
		_request_params = request.data
		try:
			chanel = Chanel.objects.get(identifier=_request_params.get('identifier'))
		except Chanel.DoesNotExist:
			return JsonResponse(data={'msg': 'chanel Dose not exists', 'success': False}, status=HTTP_404_NOT_FOUND)
		self.check_object_permissions(request, chanel)
		try:
			author = User.objects.get(username=_request_params.get('username'))
		except User.DoesNotExist:
			return JsonResponse(data={'msg': 'user not found', 'success': False}, status=HTTP_400_BAD_REQUEST)
		try:
			Chanel.objects.get(identifier=_request_params.get('identifier'), author=author)
			return JsonResponse(data={'msg': 'user is already your author ', 'success': False},
			                    status=HTTP_400_BAD_REQUEST)
		except Chanel.DoesNotExist:
			chanel.author.add(author)
			return JsonResponse(data={'msg': 'user add to your chanel author ', 'success': True},
			                    status=HTTP_201_CREATED)

	def delete(self, request, author):
		_request_params = request.data
		try:
			chanel = Chanel.objects.get(identifier=_request_params.get('identifier'), owner=request.user)
		except Chanel.DoesNotExist:
			return JsonResponse(data={'msg': 'chanel Dose not exists', 'success': False}, status=HTTP_404_NOT_FOUND)
		self.check_object_permissions(request, chanel)
		try:
			author = User.objects.get(username=author)
		except User.DoesNotExist:
			return JsonResponse(data={'msg': 'Author Dose not exists', 'success': False}, status=HTTP_404_NOT_FOUND)
		try:
			chanel = Chanel.objects.get(identifier=_request_params.get('identifier'), owner=request.user, author=author)
		except Chanel.DoesNotExist:
			return JsonResponse(data={'msg': 'Author Dose not exists', 'success': False}, status=HTTP_404_NOT_FOUND)
		chanel.author.remove(author)
		return JsonResponse(data={'msg': 'Author {} removed'.format(author.username), 'success': True},
		                    status=HTTP_404_NOT_FOUND)
