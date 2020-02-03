from django.urls import path
from .views import FileUpload
urlpatterns = [
    path('', FileUpload.as_view()),
]
