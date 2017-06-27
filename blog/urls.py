from django.conf.urls import url, include

from . import views
from blog.models import Post


urlpatterns = [
    url(r'^$', views.show_posts, name="show_posts"),
    url(r'^list$', views.show_posts, name="show_posts"),
    url(r'^(?P<pk>\d+)$', views.post_detail, name="post_detail"),
    url(r'^edit/(?P<pk>\d+)$', views.post_edit, name="post_edit"),
    url(r'^delete/(?P<pk>\d+)$', views.post_delete, name="post_delete"),
    url(r'^create/$', views.post_create, name="post_create"),
    url(r'^froala_editor/', include('froala_editor.urls')),

    # url(r'^(?P<pk>\d+)$', views.detail, name="detail"),
]
