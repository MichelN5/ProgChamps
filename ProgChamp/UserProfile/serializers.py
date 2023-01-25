from pyexpat import model
from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserProfile
        fields= ('id',
                 'profile_pic',
                 'get_profile',
                 'created_at',
                 'user')

    def create(self,validated_data):
        print(validated_data)
        addedprofile = UserProfile.objects.create(**validated_data)
        return addedprofile


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ('__all__')

