from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    message = models.CharField(blank=False, max_length=50)
    image = models.ImageField(upload_to='posts/', blank=True, height_field=None, width_field=None, max_length=None)
    # liked = models.ManyToManyField(User, related_name='likes', blank = True)
    # comments = models.ManyToManyField(User, related_name='comments', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message[:20])
    
    def num_likes(self):
        like_obj = self.like_set.all()
        count = 0
        for item in like_obj:
            if item.value == 'Like':
                count+=1
        return count
    # NO  OF COMMENTS HERE
    def num_comments(self):
        return self.comment_set.all().count()
    
    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("profiles:home")



LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -- {self.post} -- {self.value}"
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=300, blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:20] + "..."
    