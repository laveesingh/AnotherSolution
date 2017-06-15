from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post
from .forms import PostForm


def show_posts(request):
    return render(request, 'blog/show_posts.html', {'object_list': Post.objects.all().order_by('-last_edit_date'), 'all': True})


def post_detail(request, pk):
    return render(request, 'blog/post_detail.html', {'post': Post.objects.filter(id=pk)[0]})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
    form = PostForm()
    context = {
        'form': form,
        'callback': 'Create',
    }
    return render(request, 'blog/post_create.html', context)

def post_edit(request, pk=None):
    instance = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
        'callback': 'Edit',
    }
    return render(request, 'blog/post_create.html', context)