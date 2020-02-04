from django.db.models import Q
from accounts.models import User
from accounts.serializers import UserSerializer
from chanel.models import Chanel
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from chanel.serializers import ChanelSerializer
from posts.models import Post
from posts.serializers import PostSerializer


class Search(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		body = request.data.get('body')
		result = {}
		post_records = Post.objects.filter(Q(title__icontains=body) | Q(body__icontains=body))
		result['post'] = PostSerializer(post_records, many=True).data
		chanel_records = Chanel.objects.filter(Q(description__icontains=body) | Q(identifier__icontains=body))
		result['chanel'] = ChanelSerializer(chanel_records, many=True).data
		user_records = User.objects.filter(Q(first_name__icontains=body) | Q(last_name__icontains=body) |
		                                   Q(email__icontains=body) | Q(username__icontains=body))
		result['user'] = UserSerializer(user_records, many=True).data
		return JsonResponse(data={'data': result, 'success': True}, status=HTTP_200_OK)
