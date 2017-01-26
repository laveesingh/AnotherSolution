# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('body', models.TextField()),
                ('last_edit', models.CharField(max_length=200)),
                ('date', models.DateTimeField(null=True)),
                ('last_edit_date', models.DateTimeField(null=True)),
            ],
        ),
    ]
