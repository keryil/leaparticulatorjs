# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 22:42
from __future__ import unicode_literals

from django.db import migrations
import experiment.models, experiment.fields


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0010_auto_20160511_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meaning',
            name='image',
            field=experiment.fields.UploadedMeaningField(upload_to=b''),
        ),
    ]
