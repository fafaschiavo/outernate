# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160307181939 on 2016-05-07 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=400)),
                ('type_image', models.CharField(max_length=200)),
                ('member_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('newsletter_accepted_at', models.DateTimeField(auto_now_add=True)),
                ('push_accepted_at', models.DateTimeField(auto_now_add=True)),
                ('hash_id', models.CharField(default=None, max_length=200)),
            ],
        ),
    ]
