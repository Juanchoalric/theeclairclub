# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Recipe

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = "all_recipes"
    def get_queryset(self):
        return Recipe.objects.all()


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'home/detail.html'
## def index(request):
##    all_recipes = Recipe.objects.all().order_by("-date")
##    context = {"all_recipes": all_recipes}
##    return render(request, "home/home.html", context)

##def detail(request, recipe_id):
##    recipe = get_object_or_404(Recipe, pk=recipe_id)
##    return render(request, "home/detail.html", {'recipe' : recipe})
