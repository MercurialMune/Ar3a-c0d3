# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0002_remove_profile_neighborhood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='resident',
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
