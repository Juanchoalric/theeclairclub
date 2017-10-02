from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from home.models import Recipe

app_name = "category"

urlpatterns = [
    # /categories/
    url(r'^$', views.CategoriesView.as_view(), name="categories"),

]
