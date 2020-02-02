from django.urls import path
from .webservice.chanelAPI import Chanels
from .webservice.followAPI import Following

urlpatterns = [
    path('', Chanels.as_view()),
    path('update/<str:identifier>', Chanels.as_view()),
    path('delete/<int:pk>', Chanels.as_view()),
    path('get/<str:identifier>', Chanels.as_view()),
    path('get', Chanels.as_view()),
    path('follow/<str:identifier>', Following.as_view()),
]
