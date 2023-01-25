
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChallengeSerializer, ChallengeSerializerGet, UserCompletedChallengeSerializer, UserCompletedChallengeSerializerGet
from .models import Challenge, UserCompletedChallenge
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status,authentication, permissions
from rest_framework import viewsets, filters, generics
from django.db.models import Q



# Create your views here.

class ChallengesView(APIView):
    def get(self, request, format=None):
        challenges= Challenge.objects.all()
        serializer= ChallengeSerializerGet(challenges,many=True)
        return Response(serializer.data)

class ChallengeDetailsView(APIView):
    def get_object(self,category_slug,product_slug):
        try:
             return Challenge.objects.filter(Category__slug=category_slug,).get(slug=product_slug)
        except Challenge.DoesNotExist:
            raise Http404
    def get(self, request,category_slug,product_slug, format=None):
        challenge= self.get_object(category_slug,product_slug)
        serializer= ChallengeSerializerGet(challenge)
        return Response(serializer.data)

class ChallengeById(APIView):
    def get(self, request,id, format=None):
        print(id)
        challenge= Challenge.objects.get(id=1)
        print(challenge)
        serializer= ChallengeSerializer(challenge)

        return Response(serializer.data)




class CompletedChallengesView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request ,format = None):
        comch = UserCompletedChallenge.objects.filter(user=request.user)
        serializer = UserCompletedChallengeSerializerGet(comch , many=True)
        return Response(serializer.data)
        


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def CompletedChallenge(request):
    serializer = UserCompletedChallengeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    
            
class UserCreatedChallenges(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request ,format = None):
        crch= Challenge.objects.filter(Created_by=request.user)
        serializer= ChallengeSerializerGet(crch, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def CreateChallenge(request):
    print(request)
    serializer = ChallengeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(Created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def search(request):
    query= request.data.get('query', '')

    if query:
        products= Challenge.objects.filter(Q(Title__icontains=query))
        serializer= ChallengeSerializerGet(products,many=True)
        return Response(serializer.data)
    else:
        return Response({"challenges": []})













