from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .serializers import CommentsSerializer, CommentsSerializerGet
from .models import ChallengeUserComment
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class CreateComment(generics.CreateAPIView):
    serializer_class= CommentsSerializer
    queryset= ChallengeUserComment.objects.all()

class ChallengeCommments(APIView):
    def get(self, request, chall_id , format=None):
        comments= ChallengeUserComment.objects.filter(Challenge=chall_id)
        serializer = CommentsSerializerGet(comments, many=True)
        return Response(serializer.data)


