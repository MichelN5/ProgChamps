
from django.shortcuts import render
from .serializers import UserProfileSerializer, GetUserSerializer
from .models import UserProfile
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status,authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets, filters, generics, permissions





# Create your views here.
class UserProfileList(APIView):
    def get(self, request, format=None):
        profiles= UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class UserProfileView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        profile= UserProfile.objects.filter(user=request.user.id)
        serializer = UserProfileSerializer(profile, many=True)
        return Response(serializer.data)


class UpdateProfile(generics.UpdateAPIView):
    serializer_class= UserProfileSerializer
    queryset= UserProfile.objects.all()

class CreateProfile(generics.CreateAPIView):
    serializer_class= UserProfileSerializer
    queryset= UserProfile.objects.all()
    

class GetUser(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        print(request.user)
        user= User.objects.filter(id=request.user.id)
        serializer = GetUserSerializer(user, many=True)
        return Response(serializer.data)

""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""