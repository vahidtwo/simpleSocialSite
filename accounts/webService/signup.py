from ..models import User
from django.http import JsonResponse
from rest_framework.status import (
	HTTP_201_CREATED, HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView
from ..serializers import UserSerializer
from chanel.models import Chanel
import random
from django.db.utils import IntegrityError


class Signup(APIView):
	def post(self, request):
		_request_params = request.data
		validated_data = UserSerializer(data=_request_params)
		if validated_data.is_valid():
			validated_data = validated_data.data
			validated_data['point'] = 0
			validated_data['phone_number'] = _request_params.get('phone_number')
			try:
				user = User.objects.create(**validated_data)
			except IntegrityError as e:
				return JsonResponse({'data': e.args, 'success': False}, status=HTTP_400_BAD_REQUEST)

			user.set_password(_request_params['password'])
			user.save()
			chanel_identifier = validated_data['email'].split('@')[0]
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
			data = validated_data.errors
			return JsonResponse(data, status=HTTP_400_BAD_REQUEST)
