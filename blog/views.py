from django.shortcuts import render

# Create your views here. 以下追記

def post_list(request):
    return render(request, 'blog/post_list.html', {})

