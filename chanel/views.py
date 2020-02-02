from accounts.models import User
from .models import Chanel
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
)
from .serializers import ChanelSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Helper.permission import IsOwner
from chanel.models import Chanel
import random


# Create your views here.
class Chanels(APIView):
    permission_classes = (IsAuthenticated, IsOwner)

    def post(self, request):
        _request_params = dict(request.data)
        author = request.user
        owner = author
        _request_params['author'] = author.id
        _request_params['owner'] = owner.id
        if not _request_params.get('identifier'):
            _request_params['identifier'] = str(request.user.email.split('@')[0]) + "" + str(random.randint(1, 6))
        ser = ChanelSerializer(data=_request_params)
        if ser.is_valid():
            chanel = Chanel.objects.create(**ser.data, owner=author)
            chanel.author.add(author)
            return JsonResponse(data={'msg': 'create chanel', 'success': True}, status=HTTP_201_CREATED)
        else:
            return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)

    def put(self, request, identifier):
        _request_params = dict(request.data)
        _request_params['owner'] = request.user.id
        _request_params['author'] = request.user.id
        _request_params['identifier'] = identifier
        try:
            chanel = Chanel.objects.get(identifier=identifier)
        except Chanel.DoesNotExist:
            return JsonResponse(data={'msg': 'chanel Dose not exists', 'success': False}, status=HTTP_400_BAD_REQUEST)

        ser = ChanelSerializer(chanel, data=_request_params)
        if ser.is_valid():
            ser.save()
            return JsonResponse(data={'msg': 'update chanel', 'success': True}, status=HTTP_200_OK)
        else:
            return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            chanel = Chanel.objects.get(id=pk)
            self.check_object_permissions(request, chanel)
            chanel.delete()
            return JsonResponse(data={'msg': 'delete chanel', 'success': True}, status=HTTP_201_CREATED)
        except Chanel.DoesNotExist:
            return JsonResponse(data={'msg': 'chanel Dose not exists', 'success': False}, status=HTTP_400_BAD_REQUEST)

    def get(self, request, identifier=None):
        if not identifier:
            chanel = Chanel.objects.filter(author=request.user)
            return JsonResponse(data={'data': ChanelSerializer(chanel, many=True, read_only=True).data, 'success': True}, status=HTTP_201_CREATED)
        else:
            try:
                chanel = Chanel.objects.get(identifier=identifier)
                return JsonResponse(data={'data': ChanelSerializer(chanel, read_only=True).data, 'success': True}, status=HTTP_201_CREATED)
            except Chanel.DoesNotExist:
                return JsonResponse(data={'msg': 'chanel Dose not exists', 'success': False}, status=HTTP_400_BAD_REQUEST)


