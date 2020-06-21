from django.urls import path, include
from . import views
from posts.models import Post

app_name = 'posts'

urlpatterns = [
    path('<slug>/posts/', views.PostCreateView.as_view(), name='post'),
    path('posts/like/<id>', views.LikeView.as_view(), name='like'),    
]
