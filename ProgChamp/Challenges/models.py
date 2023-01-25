
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    CategoryNameC= [
        ('PY', 'Python'),
        ('JS', 'Javascript'),
        ('C++', 'C Plus Plus'),
    ]

    CategoryName= models.CharField(choices=CategoryNameC, max_length=10, default='PY')
    slug= models.CharField(max_length=10)

    def __str__(self):
        return self.CategoryName

class Challenge(models.Model):
    Category= models.ForeignKey(Category, related_name='category',on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Created_by= models.ForeignKey(User,related_name='challenge', on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)
    Description= models.TextField(max_length=1000)
    Solution= models.TextField(max_length=1000)
    slug= models.CharField(max_length=100)
    default_code= models.TextField(max_length=300)
    testcases_code = models.TextField(max_length=500)

    def __str__(self):
        return self.Title

class UserCompletedChallenge(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} | {self.challenge.Title}"




