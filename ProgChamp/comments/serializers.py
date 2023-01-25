from rest_framework import serializers
from .models import ChallengeUserComment
from UserProfile.serializers import GetUserSerializer

class CommentsSerializerGet(serializers.ModelSerializer):
    User= GetUserSerializer(many=False)
    class Meta:
        model = ChallengeUserComment
        fields= '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeUserComment
        fields= '__all__'


