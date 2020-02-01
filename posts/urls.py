from django.urls import path
from .views import Posts
urlpatterns = [
    path('', Posts.as_view()),
    path('<int:pk>', Posts.as_view()),
]
