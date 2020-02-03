from django.urls import path
from .views import Posts, GetPost
urlpatterns = [
    path('', Posts.as_view()),
    path('get', GetPost.as_view()),
    path('<int:pk>', Posts.as_view()),
    path('chanel/<str:identifier>', Posts.as_view()),
    path('update/<int:pk>', Posts.as_view()),
    path('delete/<int:pk>', Posts.as_view()),
]
