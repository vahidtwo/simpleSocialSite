from .models import Post
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
)
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Helper.permission import IsOwner
from chanel.models import Chanel


class Posts(APIView):
    permission_classes = (IsAuthenticated, IsOwner)

    def post(self, request):
        _request_params = dict(request.data)
        if not _request_params.get('chanelId'):
            return JsonResponse(data={'msg': 'chanel Does not SEND', 'success': False}, status=HTTP_400_BAD_REQUEST)
        try:
            chanel = Chanel.objects.get(pk=_request_params['chanelId'])
            self.check_object_permissions(request, chanel)
        except Chanel.DoesNotExist:
            return JsonResponse(data={'msg': 'chanel DosNotExist', 'success': False}, status=HTTP_400_BAD_REQUEST)
        _request_params['owner'] = chanel.id
        ser = PostSerializer(data=_request_params)
        if ser.is_valid():
            ser_data = ser.data
            ser_data['owner'] = chanel
            Post.objects.create(**ser_data)
            return JsonResponse(data={'msg': 'create post', 'success': True}, status=HTTP_201_CREATED)
        else:
            return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, chanel_id=None):
        if pk:
            try:
                return JsonResponse(data={'msg': PostSerializer(Post.objects.get(pk=pk)).data,
                                          'success': True}, status=HTTP_200_OK)
            except Post.DoesNotExist:
                return JsonResponse(data={'msg': 'post DosNotExist', 'success': False}, status=HTTP_400_BAD_REQUEST)
        elif chanel_id:
            pass # TODO
        else:
            _request_params = request.data
            data = PostSerializer(many=True, instance=Post.objects.filter(owner=_request_params.get('owner'))).data
            return JsonResponse(data={'msg': data, 'success': True}, status=HTTP_200_OK)
