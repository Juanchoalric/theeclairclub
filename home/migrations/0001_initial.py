# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_title', models.CharField(max_length=500)),
                ('description_one', models.TextField()),
                ('description_two', models.TextField()),
                ('description_three', models.TextField()),
                ('description_four', models.TextField()),
                ('image_one', models.FileField(upload_to=b'')),
                ('image_two', models.FileField(upload_to=b'')),
                ('image_three', models.FileField(upload_to=b'')),
                ('serves', models.CharField(max_length=100)),
                ('prep_time', models.CharField(max_length=100)),
                ('cook_time', models.CharField(max_length=100)),
                ('total_time', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('date', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Category')),
            ],
        ),
    ]
