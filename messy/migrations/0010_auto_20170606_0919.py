# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messy', '0009_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='url',
            field=models.FileField(upload_to=b'static/profile/'),
        ),
    ]