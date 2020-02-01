from django.urls import path
from .views import Chanels
urlpatterns = [
    path('', Chanels.as_view()),
    path('update/<str:identifier>', Chanels.as_view()),
    path('delete/<int:pk>', Chanels.as_view()),
    path('get/<str:identifier>', Chanels.as_view()),
    path('get', Chanels.as_view()),
]
