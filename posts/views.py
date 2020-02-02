from .models import Post
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
)
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Helper.permission import IsOwner, IsAuthorOwner
from chanel.models import Chanel


class Posts(APIView):
    permission_classes = (IsAuthenticated, IsAuthorOwner)

    def post(self, request):
        _request_params = dict(request.data)
        if not _request_params.get('chanelIdentifier'):
            return JsonResponse(data={'msg': 'chanelIdentifier Does not SEND', 'success': False}, status=HTTP_400_BAD_REQUEST)
        try:
            chanel = Chanel.objects.get(identifier=_request_params.get('chanelIdentifier'))
            self.check_object_permissions(request, chanel)
        except Chanel.DoesNotExist:
            return JsonResponse(data={'msg': 'chanel DosNotExist', 'success': False}, status=HTTP_400_BAD_REQUEST)
        _request_params['chanel'] = chanel.id
        _request_params['author'] = request.user.id
        ser = PostSerializer(data=_request_params)
        if ser.is_valid():
            ser_data = ser.data
            ser_data['chanel'] = chanel
            ser_data['author'] = request.user
            Post.objects.create(**ser_data)
            return JsonResponse(data={'msg': 'create post', 'success': True}, status=HTTP_201_CREATED)
        else:
            return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, identifier=None):
        if pk:
            try:
                return JsonResponse(data={'msg': PostSerializer(Post.objects.get(pk=pk)).data,
                                          'success': True}, status=HTTP_200_OK)
            except Post.DoesNotExist:
                return JsonResponse(data={'msg': 'post DosNotExist', 'success': False}, status=HTTP_400_BAD_REQUEST)
        elif identifier:
            return JsonResponse(data={'msg': PostSerializer(Post.objects.filter(chanel__identifier=identifier),
                                                            many=True).data, 'success': True}, status=HTTP_200_OK)
        else:
            _request_params = request.data
            data = PostSerializer(many=True, instance=Post.objects.filter(owner=_request_params.get('owner'))).data
            return JsonResponse(data={'msg': data, 'success': True}, status=HTTP_200_OK)

    def put(self, request, pk):
        _request_params = dict(request.data)
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(request, post)
            _request_params['chanel'] = post.chanel_id
            _request_params['author'] = post.author_id
        except Post.DoesNotExist:
            return JsonResponse(data={'msg': 'post DosNotExist', 'success': False}, status=HTTP_400_BAD_REQUEST)
        ser = PostSerializer(post, _request_params, allow_null=True)
        if ser.is_valid():
            ser.save()
            return JsonResponse(data={'msg': 'update post', 'success': True}, status=HTTP_200_OK)
        else:
            return JsonResponse(data={'msg': ser.errors, 'success': False}, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
            self.check_object_permissions(request, post)
            post.delete()
            return JsonResponse(data={'msg': 'delete post', 'success': True}, status=HTTP_200_OK)
        except Chanel.DoesNotExist:
            return JsonResponse(data={'msg': 'post Dose not exists', 'success': False}, status=HTTP_400_BAD_REQUEST)
