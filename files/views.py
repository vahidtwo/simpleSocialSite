import random

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
from rest_framework.permissions import IsAuthenticated


class FileUpload(APIView):
	permission_classes = (IsAuthenticated,)
	parser_class = (FileUploadParser,)

	def post(self, request, *args, **kwargs):
		_request_perms = request.data
		_request_perms['title'] = str(_request_perms['image'].name)
		ser = FileSerializer(data=_request_perms)

		if ser.is_valid():
			ser.save()
			return Response(ser.data, status=status.HTTP_201_CREATED)
		else:
			return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
