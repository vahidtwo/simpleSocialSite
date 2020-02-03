from django.urls import path
from .views import Comments

urlpatterns = [
    path('', Comments.as_view()),
    path('update/<int:pk>', Comments.as_view()),
    path('delete/<int:pk>', Comments.as_view()),
    path('post/<int:post_id>', Comments.as_view()),
]
