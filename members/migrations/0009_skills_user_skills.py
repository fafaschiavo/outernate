# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160307181939 on 2016-05-24 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_images_hash_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(default=None, max_length=200)),
                ('father_id', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=2000)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='user_skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('skill_id', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
    ]
