# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbanews', '0002_remove_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imgLink',
            field=models.URLField(blank=True),
        ),
    ]