"""sosial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from search.search import Search

urlpatterns = [
    path('api/account/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/chanel/', include('chanel.urls')),
    path('api/comment/', include('comment.urls')),
    path('api/like/', include('like.urls')),
    path('api/notify/', include('notify.urls')),
    path('api/search/', Search.as_view()),
]
