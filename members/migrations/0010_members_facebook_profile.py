# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160307181939 on 2016-05-24 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_skills_user_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='facebook_profile',
            field=models.CharField(default='', max_length=400),
        ),
    ]
