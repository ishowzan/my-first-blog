#--- 全面書き換え       https://tutorial.djangogirls.org/ja/django_admin/
from django.contrib import admin
from .models import Post

admin.site.register(Post)