from django.shortcuts import render, get_object_or_404
from .models import Post,Comment,Like
from django.views.generic import CreateView, DetailView, ListView, RedirectView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .forms import PostForm
# Create your views here.

class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = self.request.user.user_profile.get_user_posts()
        return context


class LikeView(RedirectView, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs.get('id'))
        user = self.request.user
        like, created = Like.objects.get_or_create(post=post, user=user)
        if not created:
            if like.value == 'Like':
                like.value = "Unlike"
                post.liked.remove(user)
            else:
                like.value = 'Like'
                post.liked.add(user)   
        else:
            like.value = 'Like'
            post.liked.add(user)
        like.save()
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, id):
        return reverse('profiles:home')