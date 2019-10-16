#posts forms
#django
from django import forms

#models
from posts.models import Post

class PostForm(forms.ModelForm):
    """ Post Form models."""

    class Meta:
        """form settings."""
        model = Post
        fields = ['user', 'profiles', 'title', 'photo']
