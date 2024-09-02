from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    user_model = get_user_model()
    queryset = user_model.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = UserSerializer