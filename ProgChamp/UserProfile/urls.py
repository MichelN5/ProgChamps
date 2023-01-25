from django.urls import path,include

from UserProfile import views

urlpatterns = [
    path('profile', views.UserProfileView.as_view()),
    path('getuser', views.GetUser.as_view()),
    path('userprofiles', views.UserProfileList.as_view()),
    path('createprofile', views.CreateProfile.as_view()),
    path('updateprofile/<str:pk>',views.UpdateProfile.as_view())
 ]