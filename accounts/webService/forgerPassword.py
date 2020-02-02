from ..models import User
from django.http import JsonResponse, HttpResponse
from rest_framework.status import (
     HTTP_404_NOT_FOUND
)
from rest_framework.views import APIView


class ForgetPassword (APIView):
    def post(self, request):
        _request_params = request.data
        try:
            user = User.objects.get(email=_request_params.get('email'))
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            #TODO send email
        except User.DoesNotExist:
            return HttpResponse('user not found . params: email:""', status=HTTP_404_NOT_FOUND)