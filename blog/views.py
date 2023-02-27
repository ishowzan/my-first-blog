from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    #--- blogを時間順に並べ替え（
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts}) 
        #---上で並べ替えたpostsをhtmlへ渡す
        #---　前の'posts'：名前　／　後ろのpostsは上の行の並べ替えたクエリの値posts


