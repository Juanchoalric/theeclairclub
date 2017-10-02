# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    category_title = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.category_title;

class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe_title = models.CharField(max_length=500)
    description_one = models.TextField()
    description_two = models.TextField()
    description_three = models.TextField()
    description_four = models.TextField()
    image_one = models.FileField()
    image_two = models.FileField()
    image_three = models.FileField()
    serves = models.CharField(max_length=100)
    prep_time = models.CharField(max_length=100)
    cook_time = models.CharField(max_length=100)
    total_time =models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.recipe_title
