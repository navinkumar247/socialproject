from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Relationship
from posts.models import Post
# Create your views here.
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = "profiles/signup.html"
    success_url = reverse_lazy('profiles:login')


class HomePage(CreateView, LoginRequiredMixin):
    model = Post
    template_name = "main/home.html"
    fields = ('message', 'image')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = self.request.user.user_profile.get_user_posts()
        context["friends_post_list"] = self.request.user.user_profile.get_friends_posts()
        return context


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "profiles/update_profile.html"
    fields = ('first_name','last_name','bio','country','dob','avatar')
    
        
    
    

    
