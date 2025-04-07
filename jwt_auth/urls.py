from django.urls import path
from .views import *
# from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user/register/', CreateUser.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='refresh'),
]
