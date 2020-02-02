from django.urls import path
from .views import Likes

urlpatterns = [
    path('', Likes.as_view()),
    path('update/<int:pk>', Likes.as_view()),
    path('delete/<int:pk>', Likes.as_view()),
    path('get/<int:post_id>', Likes.as_view()),
]
