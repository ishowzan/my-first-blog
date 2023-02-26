#--- 新規作成   https://tutorial.djangogirls.org/ja/django_urls/

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

