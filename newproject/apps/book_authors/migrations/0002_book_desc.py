# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-13 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(default='hi'),
            preserve_default=False,
        ),
    ]
