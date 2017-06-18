from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_tests, name='welcome'),
    url(r'^generate/', views.generate_case, name='generate_case'),
]
