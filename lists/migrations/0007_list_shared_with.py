# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 16:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0006_list_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='shared_with',
            field=models.ManyToManyField(related_name='shared_lists', to=settings.AUTH_USER_MODEL),
        ),
    ]