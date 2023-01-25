from django.urls import path, include
from Challenges import views


urlpatterns = [
    path('challenges/', views.ChallengesView.as_view()),
    path('challenges/<slug:category_slug>/<slug:product_slug>/', views.ChallengeDetailsView.as_view()),
    path('completedchallenges/', views.CompletedChallenge),
    path('usercomch/', views.CompletedChallengesView.as_view()),
    path('challenges/<slug:id>/', views.ChallengeById.as_view()),
    path('usercrch/', views.UserCreatedChallenges.as_view()),
    path('create/', views.CreateChallenge),
    path('search/', views.search),
    
]