# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0009_auto_20160511_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meaning',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
    ]
