# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170119_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='last_edit',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]