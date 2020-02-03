from ..models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings


class ForgetPassword(APIView):
	def post(self, request):
		_request_params = request.data
		try:
			user = User.objects.get(email=_request_params.get('email'))
			password = User.objects.make_random_password()
			subject = 'recover password'
			message = 'your password is {}'.format(password)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, 'vahidtwo@gmail.com', ]
			try:
				send_mail(subject, message, email_from, recipient_list)
			except:
				return JsonResponse({'msg': 'cant send mail try again', 'success': False},
				                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
			user.set_password(password)
			user.save()
			return JsonResponse({'msg': 'user password change and send to your email ', 'success': True},
			                    status=status.HTTP_200_OK)
		except User.DoesNotExist:
			return JsonResponse({'msg': 'user not found . params: email:""', 'success': False},
			                    status=status.HTTP_404_NOT_FOUND)
