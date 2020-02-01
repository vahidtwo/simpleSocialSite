from ..models import User
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView
from ..serializers import UserSerializer


class Signup(APIView):
    def post(self,request):
        _request_params = request.data
        validated_data = UserSerializer(data=_request_params)
        if validated_data.is_valid():
            validated_data = validated_data.data
            validated_data['point'] = 0
            user = User.objects.create(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return JsonResponse(validated_data, status=HTTP_201_CREATED)
        else:
            data = validated_data.errors
            return JsonResponse(data, status=HTTP_400_BAD_REQUEST)