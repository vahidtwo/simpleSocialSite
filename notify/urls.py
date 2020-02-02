from django.urls import path
from .views import Notifier

urlpatterns = [
    path('get/<int:pk>', Notifier.as_view()),
    path('get', Notifier.as_view()),
]
