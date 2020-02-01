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
        _request_params = request.data
        _request_params['owner'] = request.user.pk
        ser = PostSerializer(**_request_params)
        if ser.is_valid():
            Post.objects.create(ser.data)
            return JsonResponse(data={'msg': 'create post', 'success': False}, status=HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk:
            try:
                return JsonResponse(data={'msg': PostSerializer(Post.objects.get(pk=pk)).data,
                                          'success': True}, status=HTTP_200_OK)
            except Post.DoesNotExist:
                return JsonResponse(data={'msg': 'post DosNotExist', 'success': False}, status=HTTP_400_BAD_REQUEST)
        else:
            _request_params = request.data
            data = PostSerializer(many=True, instance=Post.objects.filter(owner=_request_params.get('owner'))).data
            return JsonResponse(data={'msg': data, 'success': True}, status=HTTP_200_OK)
