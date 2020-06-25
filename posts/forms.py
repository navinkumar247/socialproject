from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    message = forms.CharField(label=(""), widget=forms.Textarea(attrs={'rows':4,'cols':60, 'placeholder':"Type here"}))

    class Meta:
        model = Post
        fields = ("message","image")
