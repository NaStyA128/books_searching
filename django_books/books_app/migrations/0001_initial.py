# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_book', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('quantity_pages', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('part', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('chapter', models.CharField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_app.Book')),
            ],
        ),
    ]
