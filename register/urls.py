from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView

app_name = "register"

urlpatterns = [
    # /register/
    url(r'^$', views.UserFormView.as_view(), name="register"),

]
