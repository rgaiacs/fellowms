# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fellowms', '0013_auto_20160429_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='fellow',
            name='home_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fellow',
            name='home_lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]