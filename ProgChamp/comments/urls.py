from django.urls import path,include

from comments import views

urlpatterns = [
    path('comments/create', views.CreateComment.as_view()),
    path('comments/<slug:chall_id>/', views.ChallengeCommments.as_view())

 ]