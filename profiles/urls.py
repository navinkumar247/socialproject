from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'profiles'

urlpatterns = [
    path('home/',views.HomePage.as_view(), name='home'),
    path('',LoginView.as_view(template_name = 'profiles/login.html' ), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('updateprofile/<slug>/', views.ProfileUpdateView.as_view(), name='update'),
    path('profiledetail/<slug>/', views.ProfileDetailView.as_view(), name='profiledetail'),
    path('<sender>-<receiver>/friendrequest/', views.FriendRequest.as_view(), name='friendrequest'),
]
