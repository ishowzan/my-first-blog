#--- 変更： https://tutorial.djangogirls.org/ja/django_forms/

from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)