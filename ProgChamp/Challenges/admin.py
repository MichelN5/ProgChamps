from django.contrib import admin
from .models import Challenge, Category, UserCompletedChallenge



# Register your models here.
admin.site.register(Challenge)
admin.site.register(Category)
admin.site.register(UserCompletedChallenge)

