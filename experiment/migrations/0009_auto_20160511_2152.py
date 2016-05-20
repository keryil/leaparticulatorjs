# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 21:52
from __future__ import unicode_literals

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0008_auto_20160511_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meaningdimension',
            name='meanings',
        ),
        migrations.RemoveField(
            model_name='meaningspace',
            name='dimensions',
        ),
        migrations.AddField(
            model_name='meaningspace',
            name='meanings',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='experiment.Meaning'),
        ),
        migrations.DeleteModel(
            name='MeaningDimension',
        ),
    ]
