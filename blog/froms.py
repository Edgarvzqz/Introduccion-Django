from django import forms
from django.db import models

from .models import Post

class PostCreateForm (forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'content')