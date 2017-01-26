from django.conf.urls import url
from . import views

# Put here your url patterns here

urlpatterns = [
    url(r'^$', views.index),
]
