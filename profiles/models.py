from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField 
from django.template.defaultfilters import slugify
from .utils import get_unique_code
from django.urls import reverse
from posts.models import Post
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True,max_length=50)
    avatar = models.ImageField(default='avatar.jpg',upload_to='avatars/', 
                    height_field=None, width_field=None, max_length=None)
    bio = models.TextField(default='no bio...', max_length=254)
    dob = models.DateField(blank=True,null=True, auto_now=False, auto_now_add=False)
    country = CountryField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    friends = models.ManyToManyField(User,blank=True, related_name='friends')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + ' ' + str(self.last_name))
            ex = Profile.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = slugify(to_slug+ ' ' + str(get_unique_code()))
                ex = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = slugify(str(self.user.username))
        self.slug = to_slug
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("profiles:update", kwargs={"slug": self.slug})

    # GET ALL USER POSTS
    def get_user_posts(self):
        post_list = self.user.user_posts.all().order_by('-created')
        return post_list
 
    def get_friends_posts(self):
        friends = self.friends.all()
        friends |= User.objects.filter(username=self.user.username)
        return Post.objects.filter(author__in=friends).order_by("-created")

STATUS_CHOICES = {
    ('sent','sent'),
    ('accepted','accepted'),
}        

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return "{}--{}--{}".format(self.sender,self.receiver,self.status)
    
