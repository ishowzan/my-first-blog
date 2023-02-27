from django.shortcuts import render
from django.utils import timezone
from .models import Post

from django.shortcuts import render, get_object_or_404


def post_list(request):
    #--- blogを時間順に並べ替え（
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) 
        #---上で並べ替えたpostsをhtmlへ渡す
        #---　前の'posts'：名前　／　後ろのpostsは上の行の並べ替えたクエリの値posts


def post_detail(request, pk):                   #--- 追加：https://tutorial.djangogirls.org/ja/extend_your_application/
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})