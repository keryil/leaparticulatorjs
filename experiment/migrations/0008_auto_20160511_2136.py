# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0007_meaning_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meaning',
            name='image',
            field=models.FileField(upload_to='meanings'),
        ),
    ]
