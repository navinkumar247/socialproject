from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, RedirectView
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Relationship
from posts.models import Post
from posts.forms import PostForm
# Create your views here.
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = "profiles/signup.html"
    success_url = reverse_lazy('profiles:login')


class HomePage(CreateView, LoginRequiredMixin):
    model = Post
    template_name = "main/home.html"
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = self.request.user.user_profile.get_user_posts()
        context["friends_post_list"] = self.request.user.user_profile.get_friends_posts()
        return context


class ProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = Profile
    template_name = "profiles/update_profile.html"
    fields = ('first_name','last_name','bio','country','dob','avatar')

class ProfileDetailView(DetailView, LoginRequiredMixin):
    model = Profile
    template_name = "profiles/profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # CHECK RELATIONSHIP STATUS
        profile1 = get_object_or_404(Profile, slug=self.kwargs.get('slug'))
        profile2 = get_object_or_404(Profile, slug=self.request.user.user_profile.slug)
        relationship = Relationship.objects.filter(Q(sender=profile1, receiver=profile2)|Q(sender=profile2,  receiver=profile1))
        if relationship.exists():
            relationship_status = relationship[0].status
        else:
            relationship_status = "Add Friend"
        context["relationship_status"] = relationship_status

        # CHECK LIKE STATUS
        
        return context
    

class FriendRequest(RedirectView, LoginRequiredMixin):

    def get_redirect_url(self, **kwargs):
        return reverse('profiles:profiledetail', kwargs={'slug':self.kwargs.get('receiver')})

    def get(self, request, *args, **kwargs):

        profile1 = get_object_or_404(Profile, slug=self.kwargs.get('sender'))
        profile2 = get_object_or_404(Profile, slug=self.kwargs.get('receiver'))
        
        relationship = Relationship.objects.filter(Q(sender=profile1, receiver=profile2)|Q(sender=profile2,  receiver=profile1))
        if relationship.exists():
            if relationship[0].status ==  'sent':
                relationship[0].delete()
            else:
                relationship[0].delete()
                profile1.friends.remove(profile2.user)
                profile2.friends.remove(profile1.user)            
        else:
            relationship, created = Relationship.objects.get_or_create(sender=profile1, receiver=profile2)
            relationship.status = 'sent'
            relationship.save()
        return super().get(request, *args, **kwargs)
        


    
