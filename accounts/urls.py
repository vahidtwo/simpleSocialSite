from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .webService.signup import Signup
from .webService.forgerPassword import ForgetPassword
from .webService.changePassword import ChangePassword
from .webService.userAPI import UserAPI


urlpatterns = [
    path('login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup', Signup.as_view()),
    path('forgetPassword', ForgetPassword.as_view()),
    path('changePassword', ChangePassword.as_view()),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('update', UserAPI.as_view()),
    path('get/<str:username>', UserAPI.as_view()),
    path('me', UserAPI.as_view()),
]
