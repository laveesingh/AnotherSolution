from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post


def show_posts(request):
    return render(request, 'blog/show_posts.html', {'object_list': Post.objects.all().order_by('-last_edit_date'), 'all': True})


def post_detail(request, pk):
    return render(request, 'blog/post_detail.html', {'post': Post.objects.filter(id=pk)[0]})
