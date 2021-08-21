from .serializers import UserProfileSerializer, UserSerializer
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework import status as httpStatus
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import authentication

# Create your views here.

from .models import UserProfile


class LoginView(APIView):
    authentication_classes = [authentication.SessionAuthentication]

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get("username")
        password = data.get("password")
        if username is None or password is None:
            return Response(
                {"status": False, "message": "Please enter username and password"},
                status=httpStatus.HTTP_404_NOT_FOUND,
            )
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(
                {"status": True, "message": "Successfully logged in"},
                status=httpStatus.HTTP_200_OK,
            )
        return Response(
            {"status": False, "message": "Invalid credentials"},
            status=httpStatus.HTTP_401_UNAUTHORIZED,
        )


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
    model = User
    permission_classes = [AllowAny]

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"status":True,'message':"Successfully logged out"},status=httpStatus.HTTP_200_OK)
class UserProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        qs = UserProfile.objects.filter(user__id=self.request.user.id)
        return qs

    permission_classes = [IsAuthenticated]
    model = UserProfile


class CreateProfileView(CreateAPIView):
    def get_queryset(self):
        qs = UserProfile.objects.get(user__id=self.request.user.id)
        return qs

    permission_classes = [IsAuthenticated]
    model = UserProfile
    serializer_class = UserProfileSerializer
