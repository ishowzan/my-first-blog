from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post

from django.shortcuts import render, get_object_or_404
from .forms import PostForm


def post_list(request):
    #--- blogを時間順に並べ替え（
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) 
        #---上で並べ替えたpostsをhtmlへ渡す
        #---　前の'posts'：名前　／　後ろのpostsは上の行の並べ替えたクエリの値posts


def post_detail(request, pk):                   #--- 追加：https://tutorial.djangogirls.org/ja/extend_your_application/
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):                          #--- 追加： https://tutorial.djangogirls.org/ja/django_forms/
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request, pk):                     #--- 追加： https://tutorial.djangogirls.org/ja/django_forms/
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():                     #--- formの保存
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})