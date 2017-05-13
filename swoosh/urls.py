from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.get_name, name='get_name'),
    # url(r'^$', views.index, name="index"),
    url(r'^name/', views.get_name, name='get_name'),
    url(r'^plot/', views.matplot, name='matplot')
]
