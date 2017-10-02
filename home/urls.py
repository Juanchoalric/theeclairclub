from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from .models import Recipe

app_name = "home"

urlpatterns = [
    # /home/
    url(r'^$', views.IndexView.as_view(), name="index"),

    #/home/109/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
]
