

from rest_framework import serializers

from .models import Challenge,Category, UserCompletedChallenge



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=(
            'id',
            'CategoryName',
            'slug',
        )


class ChallengeSerializerGet(serializers.ModelSerializer):
    Category= CategorySerializer(many=False)
    class Meta:
        model= Challenge
        fields='__all__'

class ChallengeSerializer(serializers.ModelSerializer):

    class Meta:
        model= Challenge
        fields='__all__'

    def create(self,validated_data):
        challengecr= Challenge.objects.create(**validated_data)
        return challengecr



class UserCompletedChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserCompletedChallenge

        fields= (
            "id",
            "challenge",
        )
    

class UserCompletedChallengeSerializerGet(serializers.ModelSerializer):
    challenge= ChallengeSerializerGet(many=False)

    class Meta:
        model  = UserCompletedChallenge

        fields= (
            "id",
            "challenge",
        )
    def create(self,validated_data):
        ComCh= UserCompletedChallenge.objects.create(**validated_data)
        return ComCh





