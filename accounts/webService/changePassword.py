from ..models import User
from django.http import JsonResponse
from rest_framework.status import (
     HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class ChangePassword(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        _request_params = request.data
        password = _request_params.get('password')
        if not password:
            return JsonResponse({'msg': 'password is required', 'success': False}, status=HTTP_400_BAD_REQUEST)
        try:
            user = request.user
            user.set_password(_request_params.get('password'))
            user.save()
            return JsonResponse({'msg': 'password change', 'success': True})
        except User.DoesNotExist:
            return JsonResponse({'msg': 'user not found . params: email:""', 'success': False}, status=HTTP_400_BAD_REQUEST)