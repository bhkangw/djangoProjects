# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-13 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Users',
        ),
    ]
