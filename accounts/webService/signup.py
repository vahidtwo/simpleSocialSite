from django.http import JsonResponse
from rest_framework.status import (
	HTTP_201_CREATED, HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView
from ..serializers import UserSerializer
from chanel.models import Chanel
import random
from django.db.utils import IntegrityError
from rest_framework.parsers import FileUploadParser


class Signup(APIView):
	parser_class = (FileUploadParser,)

	def post(self, request):
		_request_params = request.data
		try:
			_request_params['title'] = str(_request_params.get('picture').name)
		except Exception:
			pass
		ser = UserSerializer(data=_request_params)
		if ser.is_valid():
			try:
				user = ser.save()
				validated_data = ser.data
			except IntegrityError as e:
				return JsonResponse({'data': e.args, 'success': False}, status=HTTP_400_BAD_REQUEST)

			user.set_password(_request_params['password'])
			user.save()
			chanel_identifier = user.username
			owner_id = user.id
			description = 'main page of {}'.format(chanel_identifier)
			try:
				chanel = Chanel.objects.create(identifier=chanel_identifier, owner_id=owner_id, description=description)

			except IntegrityError:
				chanel = Chanel.objects.create(identifier=chanel_identifier + int(random.random * 10),
				                               owner_id=owner_id,
				                               description=description)
			chanel.author.add(user)
			return JsonResponse({'data': validated_data, 'success': True}, status=HTTP_201_CREATED)
		else:
			data = ser.errors
			return JsonResponse(data, status=HTTP_400_BAD_REQUEST)
