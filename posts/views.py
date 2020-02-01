from .models import Post
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
)
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Helper.permission import IsOwner


class Posts(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        _request_params = dict(request.data)
        print(request.user.pk, type(_request_params))
        _request_params['owner'] = request.user.pk
        ser = PostSerializer(data=_request_params)
        if ser.is_valid():
            ser_data = ser.data
            ser_data['owner'] = request.user
            Post.objects.create(**ser_data)
            return JsonResponse(data={'msg': 'create post', 'success': True}, status=HTTP_201_CREATED)
        else:
            return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, chanel=None):
        if pk:
            try:
                return JsonResponse(data={'msg': PostSerializer(Post.objects.get(pk=pk)).data,
                                          'success': True}, status=HTTP_200_OK)
            except Post.DoesNotExist:
                return JsonResponse(data={'msg': 'post DosNotExist', 'success': False}, status=HTTP_400_BAD_REQUEST)
        elif chanel:
            pass # TODO
        else:
            _request_params = request.data
            data = PostSerializer(many=True, instance=Post.objects.filter(owner=_request_params.get('owner'))).data
            return JsonResponse(data={'msg': data, 'success': True}, status=HTTP_200_OK)
