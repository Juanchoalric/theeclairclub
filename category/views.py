# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from home.models import Category

# Create your views here.
##def category(request):
##    all_categories = Category.objects.all()
##    context = { 'all_categories': all_categories}
##    return render(request, "category/categories.html", context)

class CategoriesView(generic.ListView):
    template_name = 'category/categories.html'
    context_object_name = "all_categories"
    def get_queryset(self):
        return Category.objects.all()
