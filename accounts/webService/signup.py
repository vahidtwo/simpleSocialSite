from ..models import User
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView
from ..serializers import UserSerializer
from chanel.models import Chanel
from django.db.utils import IntegrityError
import random

class Signup(APIView):
    def post(self, request):
        _request_params = request.data
        validated_data = UserSerializer(data=_request_params)
        if validated_data.is_valid():
            validated_data = validated_data.data
            validated_data['point'] = 0
            user = User.objects.create(**validated_data)
            user.set_password(_request_params['password'])
            user.save()
            chanel_identifier= validated_data['email'].split('@')[0]
            owner_id = user.id
            description = 'main page of {}'.format(chanel_identifier)
            try:
                Chanel.objects.create(identifier=chanel_identifier, owner_id=owner_id, description=description)
            except IntegrityError:
                Chanel.objects.create(identifier=chanel_identifier+int(random.random*10), owner_id=owner_id,
                                      description=description)
            return JsonResponse(validated_data, status=HTTP_201_CREATED)
        else:
            data = validated_data.errors
            return JsonResponse(data, status=HTTP_400_BAD_REQUEST)