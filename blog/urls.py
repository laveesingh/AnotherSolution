from django.conf.urls import url, include

from . import views
from blog.models import Post


urlpatterns = [
    url(r'^$', views.show_posts, name="show_posts"),
    url(r'^list$', views.show_posts, name="show_posts"),
    url(r'^details/(?P<pk>\d+)$', views.post_detail, name="post_detail"),
    # url(r'^(?P<pk>\d+)$', views.detail, name="detail"),
]
