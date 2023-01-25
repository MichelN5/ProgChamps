from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User
from Challenges.models import Challenge

# Create your models here.

class ChallengeUserComment(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    Comment= models.TextField(max_length=500)


    def __str__(self):
        return f'{self.Challenge.Title} | {self.User.username} '



