from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Post
from .forms import PostForm
from .notify import (
    send_post_create_notification,
    got_hit_notification
)


def show_posts(request):
    # got_hit_notification(page="blog/show_posts")
    return render(request, 'blog/show_posts.html', {'object_list': Post.objects.all().order_by('-last_edit_date'), 'all': True})


def post_detail(request, pk):
    # got_hit_notification(page="blog/post_detail")
    return render(request, 'blog/post_detail.html', {'post': Post.objects.filter(id=pk)[0]})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            # send_post_create_notification(form);
            instance.save()
            # return HttpResponseRedirect(instance.get_absolute_url())
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

def post_delete(request, pk=None):
    user = request.user
    message = '<div class="alert alert-%s alert-dismissible" role="alert"><strong>%s!</strong> %s</div>'

    if user.is_authenticated and user.is_superuser:
        instance = get_object_or_404(Post, id=pk)
        instance.delete();
        message = message % ('success', "Success", 'Successfully deleted!')
        return JsonResponse({'message': message, 'status': 'deleted'})
    else:
        message = message % ('danger', "Error", "You can't delete that post!")
        return JsonResponse({'message': message, 'status': 'not deleted'})