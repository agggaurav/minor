# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0007_auto_20161104_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]