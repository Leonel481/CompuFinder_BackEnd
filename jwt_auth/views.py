from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data["access"]
        
        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            secure=False,  # Cambia a True en producción
            samesite='Lax'  # Ajusta según tus necesidades
        )
        
        return response

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == status.HTTP_200_OK:
            refresh_token = response.data["refresh"]
            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True,
                secure=False,  # Cambia a True en producción
                samesite='Lax'  # Ajusta según tus necesidades
            )
        
        return response