from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.


def index(request):
    return render(request, 'blog/index.html', {'object_list': Post.objects.all().order_by('-last_edit_date')})


def detail(request, pk):
    return render(request, 'blog/post.html', {'post': Post.objects.filter(id=pk)[0]})
