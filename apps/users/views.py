from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .serializers import RegisterSerializer, LoginSerializer
from django.db import IntegrityError
from .models import User


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            username_data = serializer.validated_data['username']
            email_data = serializer.validated_data['email']
            existing_username_user = User.objects.filter(username=username_data).first()
            if existing_username_user:
                return Response({'error': "Пользователь с таким именем пользователя уже существует"},
                                status=status.HTTP_400_BAD_REQUEST)

            existing_email_user = User.objects.filter(email=email_data).first()
            if existing_email_user:
                return Response({'error': "Пользователь с такой электронной почтой уже существует"},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, username=serializer.validated_data.get('username'),
                                password=serializer.validated_data.get('password'))


            if user:
                print("Пользователь успешно аутентифицирован:", user.username)
                refresh = RefreshToken.for_user(user)
                access = AccessToken.for_user(user)

                return Response({
                    "access": str(access),
                    "refresh": str(refresh)
                }, status=status.HTTP_200_OK)
            else:
                print("Неверные учетные данные.")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)