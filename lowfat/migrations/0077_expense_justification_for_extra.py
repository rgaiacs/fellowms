# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0076_auto_20160819_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='justification_for_extra',
            field=models.TextField(blank=True, max_length=120),
        ),
    ]
