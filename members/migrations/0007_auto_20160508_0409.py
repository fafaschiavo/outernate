# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160307181939 on 2016-05-08 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_members_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='email_activated',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='members',
            name='phone_activated',
            field=models.IntegerField(default=0),
        ),
    ]
